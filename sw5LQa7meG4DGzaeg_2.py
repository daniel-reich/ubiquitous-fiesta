
def multiply(lst = []):
  return lambda n: list(map(lambda num: num * n, lst))

