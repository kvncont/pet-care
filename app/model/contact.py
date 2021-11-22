from pydantic import BaseModel


class Contact(BaseModel):
    email: str
    phone: str