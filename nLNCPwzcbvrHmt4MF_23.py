
def fibonacci_sequence():
  l = [0, 1]
  while l[-1] < 200:
    l.append(l[-1] + l[-2])
  return l

