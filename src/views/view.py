import logging
from typing import List

from fastapi import APIRouter

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.operators.postgres import (
    insert_images_info,
    send_images_info
)
from src.modules import px500_parser


router = APIRouter(prefix="")


@router.get("/")
async def root():

    return 'Сервис для парсинга фотографий с сайтов для дальнейшего обучения модели для генерации фотографий' \
           'Версия 0.0.1'


@router.get("/start_parsing")
async def start_parsing():
    px500_parser.start_parsing()

    return "Успешно спаршено <ссылка на страницу>"


@router.post("/send_data")
async def send_data(body: List[ImagesInfoSchema]):
    logging.warning(body)
    send_images_info.execute(body)
