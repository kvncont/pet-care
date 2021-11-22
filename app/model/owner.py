from typing import List, Optional

from pydantic import BaseModel

from ..model.adreess import Address
from ..model.contact import Contact


class Owner(BaseModel):
    id: Optional[str] = None
    name: str
    last_name: str
    address: Optional[Address] = None
    contact: Optional[Contact] = None
