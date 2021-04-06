
def split(x):
  if x == 1:
    return 1
  from math import e
  num = int(x / e + 0.5)
  return int((x / num) ** num * 10 + 0.5) / 10

