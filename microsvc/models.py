"""Schemas"""
from pydantic import BaseModel, Field

class Message(BaseModel):
    """Class Message"""
    message: str
    to: str
    from_: str = Field(..., alias="from")
    timeToLifeSec: int
