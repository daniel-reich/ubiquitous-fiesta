
import calendar
from dateutil.relativedelta import relativedelta
def months_interval(dateStart, dateEnd):
  if dateStart > dateEnd:
    dateStart, dateEnd = dateEnd, dateStart
  result = [dateStart.month]
  while dateStart != dateEnd:
    dateStart = dateStart + relativedelta(months=+ 1)
    if dateStart.month not in result: result.append(dateStart.month)
  result.sort()
  for i in range(len(result)):
    result[i] = calendar.month_name[result[i]]
  return result

