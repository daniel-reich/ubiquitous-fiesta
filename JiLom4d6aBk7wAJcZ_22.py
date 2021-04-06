
def is_sastry(n):
  co = str(n) + str(n + 1)
  return (int(co) ** 0.5).is_integer()

