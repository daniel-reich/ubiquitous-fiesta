
def century_from_year(year):
  c = year//100
  if year%100:
    c += 1
  return c

