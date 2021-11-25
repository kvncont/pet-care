from typing import List, Optional

from pydantic.main import BaseModel

from ..models.deworming import Deworming
from ..models.owner import Owner
from ..models.vaccine import Vaccine


class Pet(BaseModel):
    id: Optional[str]
    name: str
    birthday: str
    is_alive: Optional[bool] = True
    breed: str
    gender: str
    color: str
    photo_path: Optional[str] = None
    owners: List[Owner]
    vaccines: Optional[List[Vaccine]] = None
    dewormings: Optional[List[Deworming]] = None
