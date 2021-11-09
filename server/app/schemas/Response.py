from typing import List
from pydantic import BaseModel
from typing import List

class ForecastResponse(BaseModel):
    predictions: List[float]
    train: List[float]