import axios from "axios";

const BASE_URL = "http://localhost:8000/api/forecast";

export const getForecast = async ({ currency, forecastDate }) => {
  try {
    const res = await axios.post(BASE_URL + `/${currency}`, {
      forecast_date: forecastDate
    });
    return {
      data: res.data,
      status: res.status
    };
  } catch (err) {
    return {
      error: err.response.data.error,
      status: err.response.status
    };
  }
};
