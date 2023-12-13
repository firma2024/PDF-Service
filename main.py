from typing import Union

from fastapi import FastAPI

from utils.pdf import get_pdf_metadata

app = FastAPI()


@app.get("/pdf-metadata")
async def read_root():
    return get_pdf_metadata("JuanPaez_CV.pdf")
