
def num_args(func):
  n = 0
  while True:
    try:
      func(*list(range(n)))
      return n
    except:
      n += 1

