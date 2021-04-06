
def magic(txt):
  m, d, y = (int(n) for n in txt.split(' '))
  return m * d in {y % 10, y % 100, y % 1000}

