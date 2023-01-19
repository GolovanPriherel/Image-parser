import logging
import time
from typing import Dict, Optional, List
import uuid
import json

import requests
from lxml import etree, html
from xml.etree.ElementTree import ElementTree, tostring

from src.models.postgres.rule34_images_info import Rule34ImagesInfoSchema, Rule34ImagesInfoListSchema
from src.settings import parser_settings
from src.modules.proxy import get_proxy
from src.objects import rule34_xpaths as xpaths
from src.operators.postgres import rule34_send_data
from src.helpers import download_photo


class Rule34Parser:
    def __init__(self):
        self.rule34_website = parser_settings.rule34_website

    def parse_photo_url(self, urls: List[str]):
        images_path = "data/images/"
        batch = []
        parsed_data = Rule34ImagesInfoSchema().dict()

        for url in urls:
            try:
                headers = {'Content-Type': 'text/html', }
                response = requests.get(self.rule34_website + url, headers=headers)
                response_data = response.content

                image_name = str(uuid.uuid1(0, 0)) + ".jpg"

                tree = html.fromstring(response_data)
                full_image_url = tree.xpath(xpaths.full_image_href)

                parsed_data["image_artists"] = tree.xpath(xpaths.image_artist)
                parsed_data["image_copyrights"] = tree.xpath(xpaths.image_copyrights)
                parsed_data["image_characters"] = tree.xpath(xpaths.image_character_tag)
                parsed_data["image_tags"] = tree.xpath(xpaths.image_tags)
                parsed_data["image_metadata"] = tree.xpath(xpaths.image_metadata_tags)
                parsed_data["image_url"] = self.rule34_website + url
                parsed_data["image_website"] = parser_settings.rule34_website
                parsed_data["image_name"] = image_name
                parsed_data["image_path"] = str(images_path + image_name)

                logging.warning(full_image_url)

                # download_photo(image_url=full_image_url[0],
                #                     image_name=image_name)

                batch.append(parsed_data)
                break
            except:
                continue

        batch = Rule34ImagesInfoListSchema.parse_obj(batch)
        logging.warning(type(batch))

        # rule34_send_data.execute(json.dumps(batch, default=str))
        # insert_images_info.execute(json.dumps(batch, default=str))
        # return batch

    def start_parsing(self):
        # req_session = get_proxy()

        # Авторизация
        # try:
        #     1 == i
        #     # self.authorization()
        #     logging.warning(f"Авторизация на сайте {xpaths.site_name}")
        # except:
        #     logging.warning(f"Парсинг без авторизации на сайте {xpaths.site_name}")

        # Парсинг
        try:
            headers = {'Content-Type': 'text/html', }
            response = requests.get(parser_settings.rule34_website_search, headers=headers)

            tree = html.fromstring(response.content)

            image_urls = tree.xpath(xpaths.picture_profile)

            for i, url in enumerate(image_urls):
                image_urls[i] = self.rule34_website + url

            self.parse_photo_url(image_urls)

            # time.sleep(5)
            # for i in range(5):
            #     links_list = self.get_page_links()
            #
            #     self.parse_photo_url(links_list)
            #
            #     if i == 0:
            #         next_url = self.chrome_driver.find_element(By.XPATH, xpaths.next_button).get_attribute("href")
            #         self.chrome_driver.get(next_url)
            #     else:
            #         next_url = self.chrome_driver.find_element(By.XPATH, xpaths.next_button_2).get_attribute("href")
            #         self.chrome_driver.get(next_url)

        except Exception as err:
            # logging.exception(err)
            print("Парсинг закончился с ошибкой")
            raise
        finally:
            print('Конец парсинга')
            # time.sleep(3)
            # self.chrome_driver.close()
