
def happy_year(year):
  c = str(year+1)
  while len(set(c)) != len(c):
    year += 1
    c = str(year+1)
  return int(c)

