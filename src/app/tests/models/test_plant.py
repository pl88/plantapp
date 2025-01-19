from app.models.plant import Plant

def test_fixture(test_db):
    test_db.query(Plant).all()
    assert test_db
    