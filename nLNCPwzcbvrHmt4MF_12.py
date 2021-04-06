
def fibonacci_sequence():
  a = [0, 1]
  n = a[-2] + a[-1]
  while n < 255:
    a.append(n)
    n = a[-2] + a[-1]
  return a

