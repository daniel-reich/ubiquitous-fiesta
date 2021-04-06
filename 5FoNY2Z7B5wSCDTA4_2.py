
def happy_year(y):
  while True:
    y += 1
    if len(set(str(y))) == 4:
      return y

