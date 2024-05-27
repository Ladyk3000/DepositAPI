from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.schemas import DepositRequest, DepositDetail
from app.utils import calculate_deposit


def test_calculate_deposit():
    deposit_request = DepositRequest(date="01.01.2022", periods=12, amount=15000, rate=5)
    expected_deposits = []
    current_date = datetime.strptime(deposit_request.date, "%d.%m.%Y")
    current_amount = deposit_request.amount
    for _ in range(deposit_request.periods):
        current_amount += current_amount * (deposit_request.rate / 100) / 12
        expected_deposits.append(DepositDetail(
            date=current_date.strftime("%d.%m.%Y"),
            amount=round(current_amount, 2)
        ))
        current_date += relativedelta(months=1)

    actual_deposits = calculate_deposit(deposit_request)

    assert len(actual_deposits) == len(expected_deposits)
    for actual, expected in zip(actual_deposits, expected_deposits):
        assert actual.date == expected.date
        assert actual.amount == expected.amount

