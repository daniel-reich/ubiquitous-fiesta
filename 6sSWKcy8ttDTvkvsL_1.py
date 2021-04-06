
from calendar import day_name
def afterNdays(days, n):
  lst = list(day_name)
  return [lst[(lst.index(i) + n) % 7] for i in days]

