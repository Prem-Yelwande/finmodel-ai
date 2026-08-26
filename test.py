from agents import *
from rich import print 

file_path = r"C:\Users\Prem\Desktop\FIN_MODEL_AI\nasdaq-aapl-2024-10K-241416806.pdff"

extractor = Doc_extractor()

response = extractor.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"Extract financial data from this file: {file_path}"
        }
    ]
})

print(response["structured_response"])