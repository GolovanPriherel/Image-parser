import requests
from lxml import html

from src.settings import parser_settings
from src.modules.proxy import get_proxy
from src.objects import rule34_xpaths as xpaths
from src.operators.postgres import rule34_url_parser


class Rule34URLSParser:
    def __init__(self):
        self.rule34_website = parser_settings.rule34_website

    def start_parsing(self):
        try:
            headers = {'Content-Type': 'text/html', }
            response = requests.get(parser_settings.rule34_website_search, headers=headers)
            tree = html.fromstring(response.content)

            # Добавление домена к урлам
            image_urls = tree.xpath(xpaths.picture_profile)
            image_urls = list(map(lambda x: self.rule34_website+x, image_urls))

            rule34_url_parser.execute(image_urls)

        except Exception as error:
            print(error)
