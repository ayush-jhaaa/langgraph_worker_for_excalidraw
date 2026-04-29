from typing import Annotated, List
from typing_extensions import TypedDict

from src.node1.node_1 import node_1_generator
from src.node2.node_2 import node_2_validator
from src.node3.node_3 import node_3_corrector

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages

class json_state(TypedDict, total=False):
    messages: Annotated[list, add_messages]
    user_input: str
    generated_json: List[dict]
    validated_json: List[dict]
    corrected_json: List[dict]


# build graph
graph = StateGraph(json_state)

graph.add_node("generator", node_1_generator)
graph.add_node("validator", node_2_validator)
graph.add_node("corrector", node_3_corrector)

# connect nodes
graph.set_entry_point("generator")
graph.add_edge("generator", "validator")
graph.add_edge("validator", "corrector")
graph.add_edge("corrector", END)

app = graph.compile()

initial_state = json_state(user_input="give all possible text types")
final_state = app.invoke(initial_state)

print(f"{i}\n" for i in final_state)

from IPython.display import Image, display

try:
    display(Image(app.get_graph().draw_mermaid_png()))
except Exception as e:
    print("error" , e)
    # This requires some extra dependencies and is optional
    pass