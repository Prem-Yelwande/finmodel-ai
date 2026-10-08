from pathlib import Path

import pandas as pd
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain_core.tools import tool


def _require_existing_file(file_path: str) -> Path:
    """Return a real file path, or raise a clear error before a loader fails."""
    if not file_path or not str(file_path).strip():
        raise ValueError("file_path must be a non-empty path")
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    return path


@tool
def file_type_detector(file_path: str) -> dict:
    """
    Detect the uploaded file type and return the extraction tool that should be used for processing it.
    """
    if not file_path or not str(file_path).strip():
        return {
            "status": "error",
            "message": "file_path must be a non-empty path",
        }

    path = Path(file_path)

    if not path.is_file():
        return {
            "status": "error",
            "message": "File not found.",
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
            "file_type": extension or "(none)",
            "message": "Unsupported file type.",
        }

    return {
        "status": "success",
        "file_name": path.name,
        "file_type": extension,
        "next_tool": tool_mapping[extension],
    }


@tool
def pdf_extractor(file_path: str) -> str:
    """Extract text from a PDF file."""
    path = _require_existing_file(file_path)
    documents = PyPDFLoader(str(path)).load()
    text = "\n".join(document.page_content for document in documents).strip()
    return text or "No extractable text found in PDF."


@tool
def excel_extractor(file_path: str) -> str:
    """Extract data from an Excel file."""
    path = _require_existing_file(file_path)
    excel_file = pd.ExcelFile(path)
    parts = []

    for sheet_name in excel_file.sheet_names:
        dataframe = pd.read_excel(path, sheet_name=sheet_name)
        parts.append(f"\n--- Sheet: {sheet_name} ---\n{dataframe.to_string(index=False)}")

    return "\n".join(parts).strip() or "Workbook has no readable sheets."


@tool
def docx_extractor(file_path: str) -> str:
    """Extract text from a DOCX file."""
    path = _require_existing_file(file_path)
    documents = Docx2txtLoader(str(path)).load()
    text = "\n".join(document.page_content for document in documents).strip()
    return text or "No extractable text found in DOCX."


@tool
def csv_extractor(file_path: str) -> str:
    """Extract data from a CSV file."""
    path = _require_existing_file(file_path)
    dataframe = pd.read_csv(path)
    if dataframe.empty:
        return "CSV file has no rows."
    return dataframe.to_string(index=False)
