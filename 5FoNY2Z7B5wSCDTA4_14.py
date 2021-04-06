
def happy_year(year):
  while len(list(set(str(year+1))))!=4:
    year = year + 1
  return year+1

