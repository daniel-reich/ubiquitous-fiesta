
def day_amount(month, year):
  days = {1: 31,
      2: 28,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31}
  if month == 2:
    if year % 4 == 0:
      if year % 100 == 0: 
        if year % 400 == 0:
          return days[month] + 1
        return days[month]
      return days[month] + 1
  return days[month]

