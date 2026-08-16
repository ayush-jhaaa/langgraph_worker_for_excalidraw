
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate

from rich.console import Console
from rich import print_json

from src.node1.system_instruction import system_instruction
from src.node1.converter import converter
# _________________________________________
import json,re

def parse_json_from_llm(s: str):
    # remove ```json ... ``` or ``` ... ``` if present
    cleaned = re.sub(r"^```(?:json)?|```$", "", s.strip(), flags=re.MULTILINE).strip()
    return json.loads(cleaned)
# _________________________________________
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
# _________________________________________

console = Console()
llm = ChatOpenRouter(
    model = "qwen/qwen3-next-80b-a3b-instruct",
    temperature = 0,
    api_key = API_KEY,
)
# _________________________________________
# from 
def genesis(state):
    user_prompt = state["user_input"]
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_instruction),
        ("human", "{user_prompt}")
    ])
    with console.status("[bold green]Generating Excalidraw JSON...", spinner="dots"):
        chain = prompt_template | llm
        response = chain.invoke({"user_prompt": user_prompt})
    
    result = response.content

    # console.print(type(result))
    # console.print(repr(result))

    data = parse_json_from_llm(result)
    # console.print(type(data))
    # Store in state
    state["generated_json"] = converter(data)

    print("genesis running succssfully")
    state["coming_from"] = "genesis"

    # cleaned = re.sub(r"^```(?:json)?|```$", "", result.strip(), flags=re.MULTILINE).strip()
    # print(data)
    # console.print(converter(data)) 
    return state

# Test run then i get from server
if __name__ == "__main__":
    input_prompt = input("Enter prompt: ")
    
    # initialize the state then print the result
    init_state = {"user_input" : input_prompt}

    state_after_node1 = genesis(init_state)
    # print(state_after_node1['generated_json'][0]['type'])