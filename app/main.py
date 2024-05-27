from fastapi import FastAPI, HTTPException
from app.schemas import DepositRequest, DepositResponse, ErrorResponse
from app.utils import calculate_deposit

app = FastAPI()


@app.post("/calculate-deposit",
          response_model=DepositResponse,
          responses={400: {"model": ErrorResponse}})
async def calculate_deposit_endpoint(deposit_request: DepositRequest):
    try:
        deposits = calculate_deposit(deposit_request)
        return DepositResponse(
            deposits=[{"date": d.date, "amount": d.amount} for d in deposits])
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
