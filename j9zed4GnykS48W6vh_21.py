
def digits(n):
  return n * len(str(n)) - int("1" * (len(str(n))))

