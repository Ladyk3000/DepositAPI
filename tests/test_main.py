import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)


def test_calculate_deposit_endpoint():

    deposit_request = {
        "date": "01.01.2022",
        "periods": 12,
        "amount": 15000,
        "rate": 5
    }

    response = client.post("/calculate-deposit", json=deposit_request)
    assert response.status_code == 200

    # Проверяем формат ответа
    assert response.json()["deposits"] is not None
    assert isinstance(response.json()["deposits"], list)

    # Проверяем, что количество вкладов соответствует запрошенному количеству периодов
    assert len(response.json()["deposits"]) == deposit_request["periods"]

    # Проверяем формат каждого вклада
    for deposit in response.json()["deposits"]:
        assert "date" in deposit
        assert "amount" in deposit
