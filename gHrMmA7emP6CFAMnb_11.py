
def is_apocalyptic(number):
  n = 2 ** number
  nn = str(n)
  c = nn.count("666")
  if c == 0:
    return "Safe"
  elif c == 1:
    return "Single"
  elif c == 2:
    return "Double"
  elif c == 3:
    return "Triple"

