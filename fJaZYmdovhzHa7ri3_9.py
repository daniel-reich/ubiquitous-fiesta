
def max_collatz(num):
  collats = [num]
  last = collats[-1]
  while last!=1:
    if last%2==0:
      collats.append(last//2)
    else:
      collats.append(last*3 + 1)
    last = collats[-1]
  return max(collats)

