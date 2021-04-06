
def happy_year(year):
  def is_happy(year):
    a = list(str(year))
    return len(set(a)) == len(a)
  
  y = year + 1
  while True:
    if is_happy(y):
      return y
    else:
      y += 1

