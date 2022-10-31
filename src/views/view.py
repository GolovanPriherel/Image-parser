from typing import List

from fastapi import APIRouter

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.operators.postgres import (
    insert_images_info
)
from src.modules import parser


router = APIRouter(prefix="")


@router.get("/")
async def root():

    return 'Сервис для парсинга фотографий с сайтов для дальнейшего обучения модели для генерации фотографий' \
           'Версия 0.0.1'


@router.get("/start_parsing")
async def start_parsing():
    parser.start_parsing()


@router.get("/insert_data")
async def insert_data():
    insert_images_info.execute()

