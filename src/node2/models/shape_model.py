from pydantic import BaseModel,Field,ConfigDict,model_validator
from typing import Literal, Optional

null = None
false = False

class Roundness(BaseModel):
    type : int
    value: Optional[float] = Field(default=None, ge=0)

    model_config = ConfigDict(extra="forbid")

class ShapeModel(BaseModel):
    id : str
    x : float
    y : float
    type : Literal["rectangle" , "diamond" , "ellipse"]
    height : Optional[float] = Field(None)
    angle : Optional[float] = None # in radians
    width : Optional[float] = Field(None)

    strokeColor : Optional[str] = Field("transparent",pattern=r'^(transparent|#[0-9a-fA-F]{6})$')
    backgroundColor: Optional[str] = Field("transparent",pattern=r'^(transparent|#[0-9a-fA-F]{6})$')
    fillStyle : Optional[Literal["solid" , "hachure" , "cross-hatch"]] = Field("hachure")
    strokeWidth : Optional[Literal[1,2,4,8]] = None
    strokeStyle : Optional[Literal["solid" , "dashed" , "dotted"]] = None
    roughness : Optional[float] = Field(1,ge = 0.001,le = 2)
    opacity : Optional[int] = Field(100, ge=0, le=100)

    roundness: Optional[Roundness] = None

    @model_validator(mode="after")
    def print_for_testing(cls, values):
        print(f"shape_model")
        return values
    
    model_config = ConfigDict(extra="forbid")
