
def evenly_divisible(a, b, c):
  lst = []
  for i in range(a,b+1):
    if i % c == 0:
      lst.append(i)
  return sum(lst)

