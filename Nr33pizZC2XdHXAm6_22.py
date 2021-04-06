
import datetime
def months_interval(dateStart, dateEnd):
  months = ['January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September', 'October',
        'November', 'December']
​
  tdelta = datetime.timedelta
  if dateStart < dateEnd:
    start = dateStart
    end = dateEnd
  else:
    start = dateEnd
    end = dateStart
​
  tdelta = end - start
​
  if int(tdelta.days / 30) >= 12:
    return months
  elif start == end:
    return [months[start.month - 1]]
  else:
    months = months * ((int(tdelta.days / 30) // 12) + 2)
    months = months[start.month - 1:(int(tdelta.days / 30) + (start.month))]
    if start.year < end.year and start.month > end.month:
      months = months[::-1]
​
  return months

