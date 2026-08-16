from collections import defaultdict

from src.node1.node_1 import genesis
from src.node2.node_2 import sentinel
from src.node4.node_4 import regen
from src.node3.node_3 import polisher

from langgraph.graph import StateGraph, END

# ________________________________________
from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class plan(TypedDict, total=False):
    messages: Annotated[list, add_messages]
    coming_from : str
    # for node_1
    user_input : str
    generated_json : dict[int,dict]

    # for node_2
    validation_errors : dict # pydantic.ValidationErrors
    is_valid : bool

    retry_count : int 
    max_retries : int # mostly 3

    valid_json : dict[int,dict]
    invalid_json : dict[int,dict]

    # for node_3
    corrected_json : dict[int,dict]

# ________________________________________

graph = StateGraph(plan)

graph.add_node("genesis", genesis)
graph.add_node("sentinel", sentinel)
graph.add_node("polisher", polisher)
graph.add_node("regen", regen)


# connect nodes and add logics

graph.set_entry_point("genesis")
graph.add_edge("genesis", "sentinel")
graph.add_edge("regen", "sentinel")

graph.add_conditional_edges("sentinel",
    lambda state: "valid" if state.get("is_valid") else "invalid",
    {
        "valid": "polisher",
        "invalid": "regen",
    },)

graph.add_edge("polisher", END)