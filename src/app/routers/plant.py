from fastapi import APIRouter, HTTPException
from sqlalchemy.orm.exc import NoResultFound

from schemas.plant_response import PlantResponse
from repositories.plant_repository import PlantRepository

router = APIRouter(responses={404: {"description": "Plant not found"}})


@router.get("/plant/{name}", response_model=PlantResponse)
def get_plant(name: str):
    repo = PlantRepository()

    try:
        plant = repo.get_by_name(name=name)
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Plant {name} not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception while getting plant {name}: {e}.")

    return plant
