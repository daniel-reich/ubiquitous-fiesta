
def happy_year(year):
  a = []
  while len(a)<4:
    year += 1
    a = set([i for i in str(year)])
  return year

