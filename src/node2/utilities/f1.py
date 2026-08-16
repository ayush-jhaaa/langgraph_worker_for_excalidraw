# from pydantic import 
from pydantic import ValidationError
##########


def f1(state) -> None:
    # main work is to divide into valid_json and invalid_json and store it in state
    generated_json = state["generated_json"]
    temp_valid_json = {}
    temp_invalid_json = {}


    