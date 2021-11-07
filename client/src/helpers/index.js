import { eachDayOfInterval } from "date-fns";

export const getDatesBetween = (startDate, endDate) => {
  let dates = eachDayOfInterval({ start: startDate, end: endDate });
  dates = dates.map((d) => d.toLocaleDateString("en-GB"));
  return dates;
};
