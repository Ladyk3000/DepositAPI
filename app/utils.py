from datetime import datetime
from typing import List
from dateutil.relativedelta import relativedelta
import calendar

from app.schemas import DepositDetail, DepositRequest


def calculate_deposit(deposit_request: DepositRequest) -> List[DepositDetail]:
    deposits = []
    current_date = datetime.strptime(deposit_request.date, "%d.%m.%Y")
    current_amount = deposit_request.amount

    for _ in range(deposit_request.periods):
        current_amount += current_amount * (deposit_request.rate / 100) / 12

        deposits.append(DepositDetail(
            date=current_date.strftime("%d.%m.%Y"),
            amount=round(current_amount, 2)
        ))

        next_month_date = current_date + relativedelta(months=1)

        if calendar.monthrange(current_date.year,
                               current_date.month)[1] == current_date.day:
            next_month_end_day = calendar.monthrange(next_month_date.year,
                                                     next_month_date.month)[1]
            current_date = next_month_date.replace(day=next_month_end_day)
        else:
            current_date = next_month_date

    return deposits
