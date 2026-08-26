from langchain_core.tools import tool
from pathlib import Path
from langchain_core.tools import tool
from langchain_community.document_loaders import PyPDFLoader


@tool
def file_type_detector(file_path: str) -> dict:
    """
    Detect the uploaded file type and return the extraction tool
    that should be used for processing it.
    """

    path = Path(file_path)

    if not path.exists():
        return {
            "status": "error",
            "message": "File not found."
        }

    extension = path.suffix.lower()

    tool_mapping = {
        ".pdf": "pdf_extractor",
        ".docx": "docx_extractor",
        ".csv": "csv_extractor",
        ".xlsx": "excel_extractor",
        ".xls": "excel_extractor",
    }

    if extension not in tool_mapping:
        return {
            "status": "error",
            "file_type": extension,
            "message": "Unsupported file type."
        }

    return {
        "status": "success",
        "file_name": path.name,
        "file_type": extension,
        "next_tool": tool_mapping[extension]
    }

@tool
def pdf_extractor(file_path: str) -> dict:
    """
    Extract text from a PDF document page by page.
    """

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    return {
        "file_type": "pdf",
        "file_path": file_path,
        "pages": [
            {
                "page": i + 1,
                "content": document.page_content
            }
            for i, document in enumerate(documents)
        ]
    }

from langchain_core.tools import tool
from langchain_community.document_loaders import PyPDFLoader


@tool
def pdf_extractor(file_path: str) -> str:
    """Extract text from a PDF file."""

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text = ""

    for document in documents:
        text += document.page_content + "\n"

    return text