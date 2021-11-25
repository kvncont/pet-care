from typing import List, Optional

from pydantic import BaseModel

from ..models.adreess import Address
from ..models.contact import Contact


class Owner(BaseModel):
    id: Optional[str] = None
    name: str
    last_name: str
    address: Optional[Address] = None
    contact: Optional[Contact] = None
