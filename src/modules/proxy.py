import requests
from lxml import html

from src.objects import proxy_xpath
from src.settings import parser_settings

# Получение 300 бесплатных proxy
response = requests.get(parser_settings.proxy_url).text
tree = html.fromstring(response)
proxies = tree.xpath(proxy_xpath.proxy_info)

# Подключение к прокси
session = requests.Session()
session.proxies = {"https": proxies[0]}

# Проверка прокси
print(type(str(proxies[0])))
print(str(proxies[0]))

ses = session.get("http://icanhazip.com", timeout=1.5).text.strip()
print(type(ses))
print(ses)

if str(proxies[0]) == session.get("http://icanhazip.com", timeout=1.5).text.strip():
    print(f"Успешно выбран прокси {proxies[0]}")
