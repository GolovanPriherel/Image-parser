import logging
from typing import Dict, Optional
from io import StringIO

import requests
from urllib.request import urlopen
from lxml import etree, html

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.objects import deviant_xpaths as xpaths
from src.settings import parser_settings


class DeviantartParser:
    def __init__(self):
        self.deviantart_url = parser_settings.deviantart_website_url

    @staticmethod
    def get_response(url: str, headers=None):
        if not headers:
            # headers = {'Content-Type': 'text/html', }

            return requests.get(url, headers)
        else:
            return requests.get(url)

    def start_parsing(self):
        response = self.get_response(self.deviantart_url, headers=None)
        response_html = response.content

        # with open('data/htmls/deviant_art', 'w') as f:
        #     f.write(response_html)

        tree = html.fromstring(response_html)

        image_url = self.deviantart_url

        if image_url:
            pass
            # TODO реализовать проверку наличия фотографии и тегов на странице, и последующий парсинг

        # author = tree.xpath(xpaths.author)[0]
        # image_title = tree.xpath(xpaths.image_title)[0]
        # image_tags = tree.xpath(xpaths.image_tags)
        # image_description = tree.xpath(xpaths.image_description)
        # image_description = ",".join(image_description)

        # logging.warning(tree)
        # TODO реализовать запись данных в очередь

        # self.chrome_driver.get(self.test_main_url)
        # elements = self.chrome_driver.find_elements(By.XPATH, xpaths.author)
        # for element in elements:
        #     logging.warning(element)
        #
        # self.chrome_driver.close()

    def get_more_links(self, next_url: str):
        pass

