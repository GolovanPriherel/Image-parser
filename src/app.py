from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.views import view

import logging


def create_app() -> FastAPI:
    app = FastAPI()

    @app.exception_handler(Exception)
    async def unicorn_exception_handler(request: Request, exc: Exception):
        logging.error(exc)
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logging.error(exc)
        return JSONResponse(
            status_code=422,
            content={"message": str(exc)},
        )

    app.include_router(
        view.router,
        prefix="",
        tags=["view"],
    )
    return app
