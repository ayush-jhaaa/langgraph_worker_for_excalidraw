import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from rich.console import Console
from rich import print_json
import json,re
from src.node1.system_prompt import system_instruction
def parse_json_from_llm(s: str):
    # remove ```json ... ``` or ``` ... ``` if present
    cleaned = re.sub(r"^```(?:json)?|```$", "", s.strip(), flags=re.MULTILINE).strip()
    return json.loads(cleaned)

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

console = Console()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = API_KEY
)
def node_1_generator(state):
    user_prompt = state["user_input"]
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_instruction),
        ("human", "{user_prompt}")
    ])
    with console.status("[bold green]Generating Excalidraw JSON...", spinner="dots"):
        chain = prompt_template | llm
        response = chain.invoke({"user_prompt": user_prompt})
    
    result = response.content

    console.print(type(result))
    data = parse_json_from_llm(result)
    console.print(type(data))
    # Store in state
    state["generated_json"] = data
    cleaned = re.sub(r"^```(?:json)?|```$", "", result.strip(), flags=re.MULTILINE).strip()
    print_json(cleaned)

    print("node_1 running succssfully")
    return state

# Test run then i get from server
if __name__ == "__main__":
    input_prompt = input("Enter prompt: ")
    
    # initialize the state then print the result
    init_state = {"user_input" : input_prompt}

    state_after_node1 = node_1_generator(init_state)
    # print(state_after_node1['generated_json'][0]['type'])