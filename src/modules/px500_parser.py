import logging
import time
import asyncio
from typing import Dict, Optional, List
from urllib.request import urlopen

import requests
from lxml import etree, html
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.objects import px500_xpaths as xpaths, px500_authorization_xpaths as authorization
from src.settings import parser_settings


class Px500Parser:
    def __init__(self):
        self.px500_url = parser_settings.px500_website_url
        self.driver_path = parser_settings.m1_driver_path

    def get_chromedriver(self):
        return Chrome(self.driver_path)

    @staticmethod
    def get_response(url: str, headers=None):
        if not headers:
            # headers = {'Content-Type': 'text/html', }

            return requests.get(url, headers)
        else:
            return requests.get(url)

    def authorization(self):
        self.chrome_driver.get(parser_settings.px500_authorization_url)
        login = self.chrome_driver.find_element(by=By.XPATH, value=authorization.login)
        login.send_keys(parser_settings.px500_login)
        time.sleep(1)
        password = self.chrome_driver.find_element(by=By.XPATH, value=authorization.password)
        password.send_keys(parser_settings.px500_password)
        time.sleep(1)
        self.chrome_driver.find_element(by=By.XPATH, value=authorization.log_in_button).click()

        return True

    @staticmethod
    def parse_photo_url(urls: List[str]):
        for url in urls:
            response = requests.get(url).content

            tree = html.fromstring(response)

            author = tree.xpath(xpaths.author)
            image_title = tree.xpath(xpaths.image_title)
            image_tags = tree.xpath(xpaths.image_tags)

            print(author, image_tags, image_title)

    def start_parsing(self):
        self.chrome_driver = self.get_chromedriver()

        # Авторизация
        # for i in range(1, 10):
        #     try:
        #         success = self.authorization()
        #     except:
        #         success = False
        #         time.sleep(5)
        #     logging.warning(f"Авторизируюсь в/во {i} раз")
        #     time.sleep(1)
        #     if success is True:
        #         break

        # Парсинг
        try:
            pass
            # if image_url:
            #     pass
            #     # TODO реализовать проверку наличия фотографии и тегов на странице, и последующий парсинг

            # TODO реализовать запись данных в очередь

            self.chrome_driver.get(self.px500_url)
            elements = self.chrome_driver.page_source
            with open('data/htmls/px500_popular', 'w') as f:
                f.write(elements)

            response = urlopen("file:///Users/ilyamanakinson/PycharmProjects/images_parser/data/htmls/px500_popular").read()
            tree = html.fromstring(response)
            pictures_urls = tree.xpath(xpaths.picture_profile)

            print("---promotka---")

            # TODO Промотка контента
            while True:
                body = self.chrome_driver.find_element('body')
                for i in range(5):
                    body.send_keys(Keys.PAGE_DOWN)

            # self.chrome_driver.get("https://500px.com/photo/1056280729/gold-of-rivendell-by-enrico-fossati")
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
            time.sleep(5)
            self.chrome_driver.close()

    def get_more_links(self, next_url: str):
        pass

