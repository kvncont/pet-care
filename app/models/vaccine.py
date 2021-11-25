from typing import Optional

from pydantic import BaseModel


class Vaccine(BaseModel):
    vet: str
    product: str
    description: Optional[str] = None
    date: str
    next_vaccine_date: Optional[str] = None