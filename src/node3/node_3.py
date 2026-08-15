from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate

from src.node3.system_instruction import system_instruction

# __________________________________________
import json,re

def parse_json_from_llm(s: str):
    # remove ```json ... ``` or ``` ... ``` if present
    cleaned = re.sub(r"^```(?:json)?|```$", "", s.strip(), flags=re.MULTILINE).strip()
    return json.loads(cleaned)
# __________________________________________
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
# __________________________________________
llm = ChatOpenRouter(
    model = "qwen/qwen3-next-80b-a3b-instruct",
    temperature = 0,
    api_key = API_KEY,
)
# __________________________________________
def regen(state):

    return state