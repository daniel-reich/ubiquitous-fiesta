
def fibonacci_sequence():
  a, b = 0, 1
  out = []
  while a < 255:
    out.append(a)
    a, b = b, b + a
  return out

