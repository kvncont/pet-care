import uuid

from fastapi import APIRouter, Response

from ..config.db import container
from ..models.pet import Pet

router = APIRouter(
    prefix="/pets",
    tags=["pets"]
)

FIND_PET_BY_ID = "SELECT * FROM c WHERE c.id='{}'"

@router.get("/")
async def find_all_pets():
    """Find all the pets in the database"""
    return list(container.read_all_items())


@router.get("/{id}")
async def find_pet_by_id(id: str):
    """Find a pet by its id"""
    for pet in container.query_items(
            query=FIND_PET_BY_ID.format(id),
            enable_cross_partition_query=True):
        return pet


@router.put("/", status_code=201)
async def upsert_pet(pet: Pet):
    """Insert or update a pet if it doesn't exist by its id"""
    if pet.id == None:
        pet.id = str(uuid.uuid4())
    return container.upsert_item(pet.dict())


@router.delete("/{id}", status_code=204)
async def delete_pet_by_id(id: str):
    """Delete a pet by its id"""
    container.delete_item(id, partition_key=id)
    return Response(status_code=204)
