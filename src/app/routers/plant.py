"""Here will be the acttual endpoint for plant

from typing import Annotated
from fastapi import APIRouter, Depends

from schemas.plant_response import PlantResponse
from repositories.plant_repository import PlantRepository

router = APIRouter(responses={404:{"description":"Plant not found"}})

@router.get("/plant/{name}", response_model=PlantResponse)
def get_plant(request: Annotated[PlantRequest, Depends()]):
    repo = PlantRepository()
    return repo.get(name=name)
"""