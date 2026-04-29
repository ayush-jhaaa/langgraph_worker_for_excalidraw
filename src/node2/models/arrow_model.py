from pydantic import BaseModel,Field,ConfigDict,model_validator
from typing import Literal, Optional,List

null = None
false = False

class TerminalModel(BaseModel):
    id : Optional[str] = None
    focus : Optional[float]
    gap : Optional[float]

class Roundness(BaseModel):
    # internal enum; typical values: 2 (slight), 3 (full), 12 (pill/ellipse)
    type: Literal[2, 3, 12]
    value: Optional[float] = Field(default=None, ge=0)

    model_config = ConfigDict(extra="forbid")


class ArrowModel(BaseModel):
    id : str
    x : float
    y : float
    width : float
    height : float
    angle : Optional[float] = None

    strokeColor : Optional[str] = Field("transparent",pattern=r'^(transparent|#[0-9a-fA-F]{6})$')
    backgroundColor: Optional[str] = Field("transparent",pattern=r'^(transparent|#[0-9a-fA-F]{6})$')
    strokeWidth : Optional[int] = None
    strokeStyle : Optional[Literal["solid" , "dashed" , "dotted"]] = None
    roughness : Optional[float] = Field(1,ge = 0.001,le = 2)
    opacity : Optional[int] = Field(100, ge=0, le=100)
    roundness: Optional[Roundness] = None

    points : List[List[float]]  # [[x1, y1], [x2, y2], ...]

    startBinding : Optional[TerminalModel]
    startArrowhead: Optional[Literal["arrow", "triangle", "circle", None]] = None

    endBinding : Optional[TerminalModel]
    endArrowhead: Optional[Literal["arrow", "triangle", "circle", None]] = None

    @model_validator(mode="after")
    def print_for_testing(cls, values):
        print("arrow_model")
        return values
    
    model_config = ConfigDict(extra="forbid")


raw = {
      "id": "connecting_arrow",
      "type": "arrow",
      "x": 400,
      "y": 50,
      "width": 100,
      "height": 80,
      "strokeColor": "#cc0000",
      "strokeWidth": 3,
      "endArrowhead": "arrow",
      "startBinding": null,
      "endBinding": null,
      "points": [
        [0, 80],
        [100, 0]  
      ]
    }


