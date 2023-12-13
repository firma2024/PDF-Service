from typing import Dict

import PyPDF2


def get_pdf_metadata(pdf_path: str) -> Dict[str, str]:
    """Get the metadata of a pdf given the path.

    Args:
        pdf_path (str): Path to the pdf.

    Returns:
        Dict[str,str]: Dictionary with the metadata.
    """
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    return pdf_reader.metadata
