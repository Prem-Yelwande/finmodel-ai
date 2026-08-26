from tools import pdf_extractor
from rich import print 
print("Starting...")

result = pdf_extractor.invoke(
    r"C:\Users\Prem\Desktop\FIN_MODEL_AI\BRSR202425.pdf"
)

print("Extraction completed!")
print("Result type:", type(result))
print("Result length:", len(result))
print("Result:", repr(result))