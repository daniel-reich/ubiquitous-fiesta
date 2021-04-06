
def happy_year(year):
  while True:
    year += 1
    if len(set(str(year))) == 4:
      return year

