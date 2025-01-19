

def test_fixture(test_db):
    test_db.query()
    assert test_db
    