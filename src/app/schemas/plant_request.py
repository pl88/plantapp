from pydantic import BaseModel


class PlantRequest(BaseModel):
    name: str
