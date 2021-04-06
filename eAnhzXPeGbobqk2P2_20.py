
def century(year):
  if year % 1000 == 0:
    n = str(int(str(year)[:2]))
  else:
    n = str(int(str(year)[:2])+1)
  return n + 'th century' if n != "21" else "21st century"

