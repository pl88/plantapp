from pydantic import BaseModel


class PlantResponse(BaseModel):
    id: int
    name: str
