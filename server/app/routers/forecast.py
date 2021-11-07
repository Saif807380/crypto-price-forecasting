from fastapi import APIRouter, status, Body
from datetime import timedelta

from schemas.currency import Currency
import helpers

router = APIRouter(
    prefix="/api/forecast",
    tags=["forecast"]
)

@router.post("/{currency}", status_code=status.HTTP_200_OK)
def forecast(currency: Currency, forecast_date: str = Body(..., embed=True)):
    """
    1. convert date from str to datetime - done
    2. load model based on currency
    3. build test set
    4. return predictions
    """
    return {"message": helpers.convert_str_to_date(forecast_date)}