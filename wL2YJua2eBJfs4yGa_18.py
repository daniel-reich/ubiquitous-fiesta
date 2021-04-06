
def babbage(n):
  i, p = 0, len(str(n))
  while True:
    m = (n + i) ** 0.5
    if m % 1 == 0:
      if n == 269696:
        return "Babbage was {}correct!".format("" if m == 99736 else "in")
      return m
    i += 10 ** p

