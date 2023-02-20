import pytest
from fastapi.testclient import TestClient
from microsvc.main import app

@pytest.fixture
def message():
    """build common body for request tests"""
    message =    {
        "message": "Any Message",
        "to": "Any Name",
        "from": "Any Source",
        "timeToLifeSec": 1
    }
    return message


@pytest.fixture
def client():
    """create test client"""
    client = TestClient(app)
    return client

