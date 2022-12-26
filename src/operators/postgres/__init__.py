from src.operators.postgres.insert_images_info import InsertImagesInfo
from src.operators.postgres.rule34_insert_images_info import Rule34SendData
from src.operators.postgres.url_parser import URLParserOperator
# from src.operators
from src.settings import parser_settings

insert_images_info = InsertImagesInfo()
rule34_send_data = Rule34SendData(parser_settings.parser_backend_url)
rule34_url_parser = URLParserOperator(parser_settings.parser_backend_url)
