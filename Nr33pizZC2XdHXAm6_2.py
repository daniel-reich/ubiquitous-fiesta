
def months_interval(dateStart, dateEnd):
  dates = [dateStart, dateEnd]
  dateStart, dateEnd = min(dates), max(dates)
​
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
​
  year_delta = dateEnd.year - dateStart.year
  month_delta = dateEnd.month - dateStart.month
  month_start_i = dateStart.month - 1
  month_end_i = dateEnd.month - 1
​
  if year_delta > 1 or (year_delta == 1 and month_delta >= 0):
    return months
  elif year_delta == 1 and month_delta < 0:
    return months[:month_end_i+1] + months[month_start_i:]
  else:
    return months[month_start_i : month_end_i+1]

