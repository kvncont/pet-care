from typing import Optional

from pydantic import BaseModel


class Deworming(BaseModel):
    product: str
    weight: str
    date: str
    next_deworming_date: Optional[str] = None
