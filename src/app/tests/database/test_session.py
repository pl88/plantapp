import pytest
from unittest.mock import patch
from database.session import get_db

@patch('database.session.SessionLocal')
def test_session(mock_session):
    session = next(get_db())

    assert session == mock_session.return_value
