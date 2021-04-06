
def repeating_cycle(n):
  if any(not n%x for x in [2,5]):
    return -1
  for i in range(1,n):
    if (10**i)%n==1:
      return i

