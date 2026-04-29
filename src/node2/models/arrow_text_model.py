from typing import Literal, Optional, List, Type
from pydantic import BaseModel,Field,ConfigDict,field_validator,model_validator

class TerminalModel(BaseModel):
    id : Optional[str] = None
    focus : Optional[float]
    gap : Optional[float]

class Roundness(BaseModel):
    # internal enum; typical values: 2 (slight), 3 (full), 12 (pill/ellipse)
    type: Literal[2, 3, 12]
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
    
    @model_validator(mode="after")
    def print_for_testing(cls, values):
        print("arrow_text_model")
        return values
    
    model_config = ConfigDict(extra="forbid")

    

class ArrowTextModel(BaseModel):
    id : Optional[str] = None
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
    label : Optional[Label] = None

    model_config = ConfigDict(extra="forbid")
