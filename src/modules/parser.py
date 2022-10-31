import logging
import requests
from typing import Dict, Optional

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
from lxml import etree

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.objects import xpaths
from src.settings import parser_settings


class Parser:
    def __init__(self):
        self.main_url = parser_settings.website_url
        # self.driver_path = parser_settings.driver_path
        # self.chrome_driver = self.init_chromedriver()

        self.test_main_url = parser_settings.test_website_url

    # def init_chromedriver(self):
    #     return Chrome(self.driver_path)

    @staticmethod
    def get_response(url: str, headers=None):
        if not headers:
            headers = {'Content-Type': 'text/html', }
            return requests.get(url, headers)
        else:
            return requests.get(url)

    def start_parsing(self):
        response = self.get_response(self.test_main_url, headers=None).text
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        tree.xpath(xpaths.image_tags)
        logging.warning(tree)
        # TODO реализовать запись данных в очередь

        # self.chrome_driver.get(self.test_main_url)
        # elements = self.chrome_driver.find_elements(By.XPATH, xpaths.author)
        # for element in elements:
        #     logging.warning(element)
        #
        # self.chrome_driver.close()

