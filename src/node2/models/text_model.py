from pydantic import BaseModel, model_validator, Field, ConfigDict
from typing import Literal, Optional

null = None
false = False

class TextModel(BaseModel):
    id : Optional[str]
    type : Literal["text"]
    x : float | int
    y : float | int

    strokeColor : Optional[str] = Field("transparent", pattern=r'^(transparent|#[0-9a-fA-F]{6})$')
    opacity : int = Field(100, ge=1, le=100)
    fontFamily : Literal[1,2,3,4]
    fontSize : int = Field(20,ge=15,le=50)

    text : str
    originalText : str

    @model_validator(mode="after")
    def ensure_texts_match(self):
        if self.text != self.originalText:
            raise ValueError("text -og_text not same node_2/text_model.py check")
        return self
    
    textAlign : Literal["center","right","left","middle"]
    containerId : Optional[str] = None

    @model_validator(mode="after")
    def print_for_testing(cls, values):
        print("text_model")
        return values
    
    model_config = ConfigDict(extra="forbid")
