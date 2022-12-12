from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_mila,
    fetch_one_mila,
    fetch_all_milim,
    update_mila,
    delete_mila,
)
from server.models.mila import (
    ErrorResponseModel,
    ResponseModel,
    MilaSchema,
    UpdateMilaModel,
)

router = APIRouter()


# New mila handler:

@router.post("/", response_description="Mila data added into the database")
async def add_Mila_data(mila: MilaSchema = Body(...)):
    mila = jsonable_encoder(mila)
    new_mila = await add_mila(mila)
    return ResponseModel(new_mila, "Mila added successfully.")

# Get all milon handler:


@router.get("/", response_description="Milon retrieved")
async def get_milon():
    milon = await fetch_all_milim()
    if milon:
        return ResponseModel(milon, "Milon data retrieved successfully")
    return ResponseModel(milon, "Empty list returned")

# Get one mila handler:


@router.get("/{id}", response_description="Mila data retrieved")
async def get_mila_data(id):
    mila = await fetch_one_mila(id)
    if mila:
        return ResponseModel(mila, "Mila data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Mila doesn't exist.")
