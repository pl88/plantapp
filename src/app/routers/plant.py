from fastapi import APIRouter

from schemas.plant_response import PlantResponse
from repositories.plant_repository import PlantRepository
router = APIRouter(responses={404: {"description": "Plant not found"}})


@router.get("/plant/{name}", response_model=PlantResponse)
def get_plant(name: str):
    repo = PlantRepository()
    return repo.get_by_name(name=name)
