
def evenly_divisible(a, b, c):
  n = 0
  for i in range(a,b+1):
    if i % c == 0:
      n+=i
  return n

