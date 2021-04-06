
def is_happy(n):
  return True if n == 1 else False if n == 4 else \
    is_happy(sum(int(x) * int(x) for x in str(n)))

