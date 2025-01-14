"""Here should be script to populate DB (usualy it should be done by migration, but for our purpose we can parse csv here)

Example:

from services.csv_parser import parse_csv
from models.plant import Plant
from repositories.plant_repository import PlantRepository

def populate_db(path_to_csv: str):
    plants_data = parse_csv(path_to_csv)
    plants = [Plant(plant_data) for plant in plants_data]
    for plant in plants:
        PlantRepository.add(plant)

    PlantRepository.db_session.commit()
"""