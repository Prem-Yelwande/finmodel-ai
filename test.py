from agents import Doc_extractor, Fin_analyst
from rich import print
from langchain_core.globals import set_verbose, set_debug
from langgraph.graph import StateGraph
from langgraph.constants import END


file_path = r"C:\Users\Prem\Desktop\FIN_MODEL_AI\nasdaq-aapl-2025-10K-251437791.pdf"


def extractor():
    """Extract financial data from the given PDF using Doc_extractor agent."""
    extracted_data = Doc_extractor().invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"Extract financial data from this file: {file_path}"
                }
            ]
        }
    )
    print(extracted_data)
    return extracted_data


if __name__ == "__main__":
    extractor()
