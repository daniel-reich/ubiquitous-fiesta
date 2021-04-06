
def months_interval(dateStart, dateEnd):
  res = []
  months = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']
  if dateStart > dateEnd:
    dateTemp = dateStart
    dateStart = dateEnd
    dateEnd = dateTemp
  for i in range(dateStart.year*12 + dateStart.month,dateEnd.year*12 + dateEnd.month + 1):
    month = months[i%12-1]
    if not month in res:
      res.append(month)
  return sorted(res, key=lambda x: months.index(x))

