from typing import Union

from fastapi import FastAPI

from utils.pdf import get_pdf_from_internet

app = FastAPI()


@app.get("/pdf-metadata")
async def read_root():
    return get_pdf_from_internet(
        "https://www.uv.mx/personal/gerhernandez/files/2011/04/historia-compuesta.pdf"
    )
