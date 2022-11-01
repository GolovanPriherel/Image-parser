import logging
import time
from typing import Dict, Optional

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

    def start_parsing(self):
        self.chrome_driver = self.get_chromedriver()

        for i in range(1, 10):
            try:
                success = self.authorization()
            except:
                success = False
                time.sleep(5)
            logging.warning(f"Логинюсь {i} раз")
            time.sleep(1)
            if success is True:
                break

        try:
            # response = self.get_response(self.test_main_url, headers=None)
            # response_html = response.content
            #
            # tree = html.fromstring(response_html)
            self.chrome_driver.get(self.px500_url)

            # if image_url:
            #     pass
            #     # TODO реализовать проверку наличия фотографии и тегов на странице, и последующий парсинг

            # author = tree.xpath(xpaths.author)[0]
            # image_title = tree.xpath(xpaths.image_title)[0]
            # image_tags = tree.xpath(xpaths.image_tags)
            # image_description = tree.xpath(xpaths.image_description)
            # image_description = ",".join(image_description)

            # logging.warning(author)
            # TODO реализовать запись данных в очередь

            # self.chrome_driver.get(self.test_main_url)
            # elements = self.chrome_driver.find_elements(By.XPATH, xpaths.author)
            # for element in elements:
            #     logging.warning(element)
            #
            # self.chrome_driver.close()
        finally:
            time.sleep(5)
            self.chrome_driver.close()

    def get_more_links(self, next_url: str):
        pass

