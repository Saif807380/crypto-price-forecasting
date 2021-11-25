import React, { useState } from "react";
import "date-fns";
import { Box, Typography } from "@material-ui/core";
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker
} from "@material-ui/pickers";
import DateFnsUtils from "@date-io/date-fns";
import { Line } from "react-chartjs-2";
import { getDatesBetween } from "../helpers";
import { getForecast } from "../actions/forecastActions";

const Bitcoin = () => {
  const [selectedDate, setSelectedDate] = useState(new Date("10/12/2021"));
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: []
  });
  const handleDateChange = (date) => {
    console.log(date.toLocaleDateString("en-GB"));
    setSelectedDate(date);
    const predictionLabels = getDatesBetween(new Date("10/12/2021"), date);
    const trainLabels = getDatesBetween(
      new Date("01/01/2021"),
      new Date("10/11/2021")
    );
    getForecast({
      currency: "btc",
      forecastDate: date.toLocaleDateString("en-GB")
    }).then((res) => {
      if (res.error) {
      } else {
        const predictionData = predictionLabels.map((label, index) => ({
          x: label,
          y: res.data.predictions[index]
        }));
        const trainData = trainLabels.map((label, index) => ({
          x: label,
          y: res.data.train[index]
        }));
        setChartData((prevData) => ({
          ...prevData,
          datasets: [
            {
              label: "Historical",
              data: trainData,
              fill: false,
              backgroundColor: "rgb(255, 165, 0)",
              borderColor: "rgba(255, 165, 0, 0.5)"
            },
            {
              label: "Forecast",
              data: predictionData,
              fill: false,
              backgroundColor: "rgb(0,90,255)",
              borderColor: "rgba(0,90,255, 0.5)"
            }
          ]
        }));
      }
    });
  };

  const options = {
    scales: {
      y: {
        beginAtZero: false,
        title: {
          display: true,
          text: "Price in USD"
        }
      },
      x: {
        title: {
          display: true,
          text: "Date"
        }
      }
    }
  };

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Box display="flex" flexDirection="column">
        <Box display="flex" justifyContent="space-between">
          <Typography
            variant="h5"
            style={{ marginRight: "16px", display: "inline" }}
          >
            Bitcoin (BTC)
          </Typography>
          <Box>
            <KeyboardDatePicker
              disableToolbar
              variant="inline"
              format="dd/MM/yyyy"
              id="date-picker-inline"
              label="Forecast Date"
              value={selectedDate}
              onChange={handleDateChange}
              KeyboardButtonProps={{
                "aria-label": "change date"
              }}
              minDate={new Date("10/12/2021")}
            />
          </Box>
        </Box>
        <Box>
          <Line data={chartData} options={options} />
        </Box>
      </Box>
    </MuiPickersUtilsProvider>
  );
};

export default Bitcoin;
