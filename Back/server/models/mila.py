from typing import Optional
from pydantic import BaseModel, Field



class MilaSchema(BaseModel):
    spanish: str = Field(...)
    hebrew: str = Field(...)
    fonetica: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "spanish": "hola",
                "hebrew": "שלום",
                "fonetica": "shalom",
            }
        }


class UpdateMilaModel(BaseModel):
    spanish: Optional[str]
    hebrew: Optional[str]
    fonetica: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "spanish": "hola",
                "hebrew": "שלום",
                "fonetica": "shalom",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
