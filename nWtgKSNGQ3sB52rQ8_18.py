
def evenly_divisible(a, b, c):
  sum = 0
  for i in range(a,b+1):
    if i%c == 0: sum += i
  return sum

