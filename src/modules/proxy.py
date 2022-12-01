import logging
import requests
from lxml import html
import random

from src.objects import proxy_xpath
from src.settings import parser_settings


# Получение 300 бесплатных proxy
def parse_proxies_site():
    response = requests.get(parser_settings.proxy_url).text
    tree = html.fromstring(response)

    proxies = tree.xpath(proxy_xpath.proxy_info)
    return proxies


# Подключение к прокси
def get_proxy():
    session = requests.Session()
    proxy_list = parse_proxies_site()
    for proxy in proxy_list:
        try:
            session.proxies = {"http": proxy, "https": proxy}
            ses = session.get("http://icanhazip.com", timeout=1.5).text.strip()
            print(f"Успешно выбран прокси {proxy}")
            return proxy
        except:
            print(f"--- pass {proxy}")
        finally:
            session.close()