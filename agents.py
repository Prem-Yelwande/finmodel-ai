from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import *
import os
from dotenv import load_dotenv
from prompts import Extractor_prompt, Financial_prompt
from states import *
from langchain_core.globals import set_verbose, set_debug
from langgraph.graph import StateGraph
from langgraph.constants import END

load_dotenv()



llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

llm1 = ChatMistralAI(
    model = "mistral-small-latest",
    api_key=os.getenv("MISTRA_AI_API_KEY"),
    temperature=0
)

def Doc_extractor():
    return create_agent(
    model=llm1,
    tools=[file_type_detector, pdf_extractor],
    system_prompt=Extractor_prompt(),
    response_format=FinancialData
)

def Fin_analyst():
    return create_agent(
        model = llm,
        system_prompt = Financial_prompt(),
        response_format = FinancialAnalysisResult

    )

    