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

const Bitcoin = () => {
  const [selectedDate, setSelectedDate] = useState(new Date("10/12/2021"));
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: []
  });
  const handleDateChange = (date) => {
    console.log(date.toLocaleDateString("en-GB"));
    setSelectedDate(date);
    const labels = getDatesBetween(new Date("10/12/2021"), date);

    setChartData((prevData) => ({
      ...prevData,
      labels: labels,
      datasets: [
        {
          label: "Forecast",
          data: Array.from({ length: labels.length }, (_, i) => i + 1),
          fill: false,
          backgroundColor: "rgb(255, 99, 132)",
          borderColor: "rgba(255, 99, 132, 0.7)"
        }
      ]
    }));
  };

  const options = {
    scales: {
      y: {
        beginAtZero: false
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
