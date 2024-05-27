import os
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize("invalid_request", [
    {"date": "01.01.2022", "periods": 12, "amount": 5000, "rate": 5},

    {"date": "01.01.2022", "periods": 0, "amount": 15000, "rate": 5},

    {"date": "01.01.2022", "periods": 12, "amount": 15000, "rate": 0},

])
def test_invalid_request(invalid_request):
    response = client.post("/calculate-deposit", json=invalid_request)
    assert response.status_code == 422
    error_detail = response.json()["detail"]
    expected_error_messages = [
        "Input should be greater than or equal to 10000",
        "Input should be greater than or equal to 1",
        "Input should be greater than or equal to 1"
    ]
    assert any(expected_error_message in error["msg"] for error in error_detail for expected_error_message in expected_error_messages)


def test_valid_request():
    valid_request = {
        "date": "01.01.2022",
        "periods": 12,
        "amount": 15000,
        "rate": 5
    }
    response = client.post("/calculate-deposit", json=valid_request)
    assert response.status_code == 200
    data = response.json()
    assert "deposits" in data
    assert len(data["deposits"]) == valid_request["periods"]
    for deposit in data["deposits"]:
        assert "date" in deposit
        assert "amount" in deposit
