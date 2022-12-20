import logging
import time
import asyncio
from typing import Dict, Optional, List
from urllib.request import urlopen
import uuid

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

    def download_photo(self, image_url: str, image_name: str):
        resource = urlopen(image_url)
        out = open(f"data/images/{image_name}.jpg", 'wb')
        out.write(resource.read())
        out.close()

    def parse_photo_url(self, urls: List[str], req_session):
        images_path = "data/images/"
        batch = []
        parsed_data = ImagesInfoSchema().dict()

        for url in urls:
            headers = {'Content-Type': 'text/html', }
            response = req_session.get(url, headers=headers)
            response_data = response.content

            image_name = str(uuid.uuid1(0, 0)) + ".jpg"

            tree = html.fromstring(response_data)
            # full_image_url = tree.xpath(xpaths.full_image_url)
            #
            # logging.warning(full_image_url)

            # self.download_photo(image_url=full_image_url,
            #                     image_name=image_name)

            parsed_data["author"] = tree.xpath(xpaths.author)
            parsed_data["image_title"] = tree.xpath(xpaths.image_title)
            parsed_data["image_tag"] = tree.xpath(xpaths.image_tags)
            parsed_data["image_description"] = tree.xpath(xpaths.image_description)
            parsed_data["image_url"] = url
            parsed_data["image_website"] = parser_settings.px500_website_url
            parsed_data["image_name"] = image_name
            parsed_data["image_path"] = str(images_path + image_name)

            # logging.warning(url)

            batch.append(parsed_data)
            logging.warning(batch)
            break

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
            # req_session = self.get_proxy_request(get_proxy())

            links_list = ['https://500px.com/photo/1057683104/morning-mood-by-andy58andras-schafer',
                          "https://500px.com/photo/1057664465/deer-in-front-of-an-old-stone-barn-by-jorn-allan-pedersen"]
            html = requests.get(links_list[0])
            self.parse_photo_url(links_list, requests)

        finally:
            pass
            # time.sleep(5)
            # self.chrome_driver.close()

    def get_more_links(self, next_url: str):
        pass

