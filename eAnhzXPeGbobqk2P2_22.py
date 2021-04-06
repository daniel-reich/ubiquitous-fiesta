
def century(year):
  if year % 100 == 0:
    x = year // 100
  else:
    x = year // 100 + 1
  if x == 21:
    return str(x) + "st century"
  return str(x) + "th century"

