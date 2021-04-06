
def fibonacci_sequence():
  l = [0,1]
  while l[-1]+l[-2]<255:
    l.append(l[-2]+l[-1])
  return l

