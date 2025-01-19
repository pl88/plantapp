import unittest
from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_get_root(self):
        r = test_client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"message": "Hello message"})

