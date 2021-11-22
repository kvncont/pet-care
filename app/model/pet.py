from typing import List, Optional

from pydantic.main import BaseModel

from ..model.deworming import Deworming
from ..model.owner import Owner
from ..model.vaccine import Vaccine


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
