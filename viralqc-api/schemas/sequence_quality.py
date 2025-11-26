from pydantic import BaseModel
from typing import List


class SequenceItem(BaseModel):
    id: str
    sequence: str


class SequenceQualityInput(BaseModel):
    sequences: List[SequenceItem]
