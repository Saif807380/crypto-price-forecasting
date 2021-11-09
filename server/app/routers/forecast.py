from fastapi import APIRouter, status, Body
from datetime import timedelta

from schemas.currency import Currency
from schemas.Response import ForecastResponse
from models.Model import Model

router = APIRouter(
    prefix="/api/forecast",
    tags=["forecast"]
)

model = Model()

@router.post("/{currency}", status_code=status.HTTP_200_OK, response_model=ForecastResponse)
def forecast(currency: Currency, forecast_date: str = Body(..., embed=True)):
    train_data = model.get_data(currency)
    predictions = model.get_predictions(currency, forecast_date)
    return ForecastResponse(predictions = predictions, train = train_data)