
def evenly_divisible(a, b, c):
  li = []
  for n in range(a,b+1):
    if n%c == 0:
      li.append(n)
  return sum(li)

