import logging
import time
import asyncio
from typing import Dict, Optional, List
from urllib.request import urlopen

import requests
from lxml import etree, html
from xml.etree.ElementTree import ElementTree, tostring
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.objects import px500_xpaths as xpaths, px500_authorization_xpaths as authorization
from src.settings import parser_settings
from src.modules.proxy import get_proxy


class Px500Parser:
    def __init__(self):
        self.px500_url = parser_settings.px500_website_url
        self.driver_path = parser_settings.m1_driver_path
        # self.driver_path = parser_settings.linux_driver_path

    def get_chromedriver(self):
        return Chrome(self.driver_path)

    @staticmethod
    def get_proxy_request(proxy):
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        return session

    @staticmethod
    def get_response(url: str, headers=None):
        if not headers:
            headers = {'Content-Type': 'text/html', }

            return requests.get(url, headers)
        else:
            return requests.get(url)

    def authorization(self):
        for i in range(1, 10):
            try:
                self.chrome_driver.get(parser_settings.px500_authorization_url)
                login = self.chrome_driver.find_element(by=By.XPATH, value=authorization.login)
                login.send_keys(parser_settings.px500_login)
                time.sleep(1)
                password = self.chrome_driver.find_element(by=By.XPATH, value=authorization.password)
                password.send_keys(parser_settings.px500_password)
                time.sleep(1)
                self.chrome_driver.find_element(by=By.XPATH, value=authorization.log_in_button).click()
                success = True
            except:
                success = False
                time.sleep(5)
            logging.warning(f"Авторизируюсь в/во {i} раз")
            time.sleep(1)
            if success is True:
                break

    def get_page_links(self):
        links_list = []
        elems = self.chrome_driver.find_elements(By.XPATH, xpaths.picture_profile)
        for elem in elems:
            links_list.append(elem.get_attribute("href"))

        return links_list

    @staticmethod
    def parse_photo_url(urls: List[str]):
        for url in urls:
            headers = {'Content-Type': 'text/html', }
            response = requests.get(url, headers=headers)
            response_data = response.text

            tree = html.fromstring(response_data)

            category = tree.xpath(xpaths.category)
            print(category)

    def start_parsing(self):
        # self.chrome_driver = self.get_chromedriver()

        # Авторизация
        try:
            1 == i
            # self.authorization()
            logging.warning(f"Авторизация на сайте {xpaths.site_name}")
        except:
            logging.warning(f"Парсинг без авторизации на сайте {xpaths.site_name}")

        # Парсинг
        try:
            pass
            # if image_url:
            #     pass
            #     # TODO реализовать проверку наличия фотографии и тегов на странице, и последующий парсинг

            # TODO реализовать запись данных в очередь

            # # Локальное скачивание
            # self.chrome_driver.get(self.px500_url)
            # elements = self.chrome_driver.page_source
            # with open('data/htmls/px500_popular', 'w') as f:
            #     f.write(elements)

            # response = urlopen("file:///Users/ilyamanakinson/PycharmProjects/images_parser/data/htmls/px500_popular").read()
            # tree = html.fromstring(response)
            # pictures_urls = tree.xpath(xpaths.picture_profile)
            # print(pictures_urls)

            # TODO Промотка контента
            # print("---promotka---")
            # self.chrome_driver.get("https://500px.com/popular")
            # self.chrome_driver.get("https://500px.com/photo/1056280729/gold-of-rivendell-by-enrico-fossati")
            # self.chrome_driver.get("https://yandex.ru/search/?text=selenium.common.exceptions.InvalidArgumentException%3A+Message%3A+invalid+argument%3A+invalid+locator&lr=39&clid=1955454")

            # while True:
                # body = self.chrome_driver.find_element(By.XPATH, '/html/body')
                # time.sleep(3)
                # for i in range(3):
                #     body.send_keys(Keys.PAGE_DOWN)
                #     time.sleep(2)
            # time.sleep(5)
            # links_list = self.get_page_links()
            # print(links_list)

            links_list = ['https://500px.com/photo/1057683104/morning-mood-by-andy58andras-schafer',
                          "https://500px.com/photo/1057664465/deer-in-front-of-an-old-stone-barn-by-jorn-allan-pedersen"]
            self.parse_photo_url(links_list)

            # self.chrome_driver.get("https://500px.com/photo/1057664465/deer-in-front-of-an-old-stone-barn-by-jorn-allan-pedersen")
            # category = self.chrome_driver.find_elements(By.XPATH, xpaths.category)
            # print(category)
            # elements = self.chrome_driver.page_source
            # with open('data/htmls/px500_photo', 'w') as f:
            #     f.write(elements)
            #

            # elements = self.chrome_driver.find_elements(By.XPATH, xpaths.picture)
            # elements = self.chrome_driver.find_elements(By.XPATH, xpaths.image_tags)
            # logging.warning(elements)
            # for element in elements:
            #     logging.warning(element)

        finally:
            pass
            # time.sleep(5)
            # self.chrome_driver.close()

    def get_more_links(self, next_url: str):
        pass

