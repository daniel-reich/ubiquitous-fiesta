
import calendar
def how_unlucky(y):
  sum = 0
  for month in range(1,13):
    if calendar.weekday(y,month,13) == 4:
      sum += 1
  return sum

