
def fibonacci_sequence():
  L = [0, 1]
  while L[-1] + L[-2] < 255:
    L.append(L[-1] + L[-2])
  return L

