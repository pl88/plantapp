from repositories.base_repository import BasePlantRepository
from models.plant import Plant


class PlantRepository(BasePlantRepository):
    model = Plant
