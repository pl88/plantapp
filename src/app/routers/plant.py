
from fastapi import APIRouter

#from repositories.plant_repository import PlantRepository

router = APIRouter()

@router.get("/plant/{name}")
def get_plant(name: str):
    return {"id": 1, "name": name}
    #repo = PlantRepository()
    #return repo.get_by_name(name=name)
