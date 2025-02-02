import pytest
from unittest.mock import patch
from app.database.session import get_db

@patch('app.database.session.SessionLocal')
def test_session(mock_session):
    session = next(get_db())

    assert session == mock_session.return_value