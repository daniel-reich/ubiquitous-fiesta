
import datetime, calendar
def months_interval(dateStart, dateEnd):
  dateStart, dateEnd = sorted([dateStart, dateEnd])
  years = dateEnd.year - dateStart.year
  val1 = dateStart.month
  val2 = min(years*12 + dateEnd.month + 1, val1 + 12)
  months = sorted([v if v < 13 else v-12 for v in range(val1,val2)])
  return [calendar.month_name[month] for month in months]

