from models.plant import Plant

def test_fixture(test_db):
    plant_to_db = Plant(id=1,name="tralala")
    test_db.add(plant_to_db)
    test_db.commit()

    plant_from_db = test_db.query(Plant).filter_by(name="tralala").one()
    
    assert test_db
    assert plant_to_db == plant_from_db
    