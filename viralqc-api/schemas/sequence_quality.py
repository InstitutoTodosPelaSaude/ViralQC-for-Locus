from pydantic import BaseModel
from typing import List


class SequenceItem(BaseModel):
    id: int
    sequence: str


class SequenceQualityInput(BaseModel):
    sequences: List[SequenceItem]
