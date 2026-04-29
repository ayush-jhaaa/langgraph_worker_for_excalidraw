from pydantic import BaseModel, ConfigDict, Field, field_validator,model_validator
from typing import Literal, Optional

null = None
false = False

class Roundness(BaseModel):
    type : int
    value: Optional[float] = Field(default=None, ge=0)

    model_config = ConfigDict(extra="forbid")

class Label(BaseModel):
    text: str
    fontSize: int = Field(..., ge=8, le=100)
    fontFamily: Literal[1, 2, 3, 4] = Field(..., description="Font family index")
    strokeColor: str = Field(
        "#000000", pattern=r"^(#[0-9a-fA-F]{6}|transparent)$"
    )
    opacity: int = Field(100, ge=0, le=100)
    textAlign: Literal["left", "center", "right", "middle"] = "center"
    verticalAlign: Literal["top", "middle", "bottom", "centre"] = "middle"

    # normalize text alignment if needed
    @field_validator("verticalAlign")
    def normalize_alignment(cls, v):
        return "middle" if v.lower() == "centre" else v
    
class ShapeTextModel(BaseModel):

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
    roughness : Optional[float] = Field(1,ge = 0,le = 2)
    opacity : Optional[int] = Field(100, ge=0, le=100)

    roundness: Optional[Roundness] = None

    label : Optional[Label] = None

    @model_validator(mode="after")
    def print_for_testing(cls, values):
        print(f"{values.type} shape_text_model")
        return values
    
    model_config = ConfigDict(extra="forbid")
    