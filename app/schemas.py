from pydantic import BaseModel, Field, conint, confloat


class DepositRequest(BaseModel):
    date: str = Field(..., pattern=r"\d{2}\.\d{2}\.\d{4}")
    periods: conint(ge=1, le=60)
    amount: conint(ge=10000, le=3000000)
    rate: confloat(ge=1, le=8)


class DepositDetail(BaseModel):
    date: str
    amount: float


class DepositResponse(BaseModel):
    deposits: list[DepositDetail]


class ErrorResponse(BaseModel):
    detail: str
