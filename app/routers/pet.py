import uuid

from fastapi import APIRouter, Response

from ..config.db import container
from ..model.pet import Pet

router = APIRouter(
    prefix="/pets",
    tags=["pets"]
)

FIND_PET_BY_ID = "SELECT * FROM c WHERE c.id='{}'"

@router.get("/")
async def find_all_pets():
    return list(container.read_all_items())


@router.get("/{id}")
async def find_pet_by_id(id: str):
    for pet in container.query_items(
            query=FIND_PET_BY_ID.format(id),
            enable_cross_partition_query=True):
        return pet


@router.put("/", status_code=201)
async def upsert_pet(pet: Pet):
    if pet.id == None:
        pet.id = str(uuid.uuid4())
    return container.upsert_item(pet.dict())


@router.delete("/{id}", status_code=204)
async def delete_pet_by_id(id: str):
    container.delete_item(id, partition_key=id)
    return Response(status_code=204)
