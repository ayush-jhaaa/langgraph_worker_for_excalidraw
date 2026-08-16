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

