
def is_sastry(n):
  return str(int(str(n) + str(n + 1)) ** 0.5).endswith("0")

