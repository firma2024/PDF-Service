import io
from typing import Dict

import PyPDF2
import requests


def get_pdf_metadata(pdf_path: str) -> Dict[str, str]:
    """Get the metadata of a pdf given the path.

    Args:
        pdf_path (str): Path to the pdf.

    Returns:
        Dict[str,str]: Dictionary with the metadata.
    """
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    return pdf_reader.metadata


def get_pdf_from_internet(url):
    response = requests.get(url)

    if response.status_code == 200:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(response.content))
        pdf_text = ""
        print(len(pdf_reader.pages))
        for page_number in range(0, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            if "Analógicas" in page.extract_text():
                pdf_text += page.extract_text()
        return pdf_text
    else:
        print(f"Failed to download the PDF file. Response code: {response.status_code}")
        return None
