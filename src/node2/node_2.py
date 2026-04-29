from langchain.output_parsers import PydanticOutputParser
# from pydantic import 

##########
from src.node2.models.shape_model import ShapeModel
from src.node2.models.shape_text_model import ShapeTextModel
from src.node2.models.text_model import TextModel
from src.node2.models.arrow_model import ArrowModel
from src.node2.models.arrow_text_model import ArrowTextModel
from src.node2.models.line_model import LineModel

# we have shape,text,shape+texxt,arrow,arrow+text,line
# we decide which validator to use
def validator_selector(json):
    type = json.get("type")
    label = json.get("label")

    if label: # then shape/arrow + text
        validator = {
            "ellipse" : ShapeTextModel,
            "diamond" : ShapeTextModel,
            "rectangle" : ShapeTextModel,
            "arrow" : ArrowTextModel,
        }
        return validator[type]
    
    else: #no label wale
        validator = {
            "ellipse" : ShapeModel,
            "diamond" : ShapeModel,
            "rectangle" : ShapeModel,
            "arrow" : ArrowModel,
            "text" : TextModel,
            "line" : LineModel
        }
        return validator[type]

test_cases = [
    {"type": "rectangle", "label": {"text": "Rectangle Label"}},
    {"type": "arrow", "label": {"text": "Arrow Label"}},
    {"type": "ellipse", "label": {"text": "Ellipse Label"}},
    {"type": "diamond", "label": {"text": "Diamond Label"}},
    {"type": "rectangle"},
    {"type": "arrow"},
    {"type": "ellipse"},
    {"type": "diamond"},
    {"type": "line"},
    {"type": "text"},
]

def node_2_validator(state):
    json_array = state["generated_json"]
    for json in json_array:
        model_class = validator_selector(json)
        validated_obj = model_class.model_validate(json)
        # print(validator)
    state["is_valid"] = True
    print('node 2 running')
    return state

init_state = {}
if __name__ == "__main__":
    node_2_validator(init_state)
