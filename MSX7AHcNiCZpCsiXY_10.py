
import calendar
def how_unlucky(y):
  count = 0
  for mon in range(1, 13):
    if calendar.weekday(y,mon,13) == 4:
      count += 1
  return count

