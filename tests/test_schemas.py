from pydantic import ValidationError
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.schemas import DepositRequest, DepositDetail, DepositResponse, \
    ErrorResponse


def test_deposit_request_valid():
    deposit_request = DepositRequest(date="01.01.2022", periods=12, amount=15000, rate=5)
    assert deposit_request.date == "01.01.2022"
    assert deposit_request.periods == 12
    assert deposit_request.amount == 15000
    assert deposit_request.rate == 5


def test_deposit_request_invalid():
    with pytest.raises(ValidationError):
        DepositRequest(date="01/01/2022", periods=12, amount=15000, rate=5)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=0, amount=15000, rate=5)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=61, amount=15000, rate=5)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=12, amount=9999, rate=5)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=12, amount=3000001, rate=5)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=12, amount=15000, rate=0)

    with pytest.raises(ValidationError):
        DepositRequest(date="01.01.2022", periods=12, amount=15000, rate=9)


def test_deposit_detail():
    deposit_detail = DepositDetail(date="01.01.2022", amount=15000.0)
    assert deposit_detail.date == "01.01.2022"
    assert deposit_detail.amount == 15000.0


def test_deposit_response():
    deposit_response = DepositResponse(deposits=[DepositDetail(date="01.01.2022", amount=15000.0)])
    assert len(deposit_response.deposits) == 1
    assert deposit_response.deposits[0].date == "01.01.2022"
    assert deposit_response.deposits[0].amount == 15000.0


def test_error_response():
    error_response = ErrorResponse(detail="Error occurred")
    assert error_response.detail == "Error occurred"
