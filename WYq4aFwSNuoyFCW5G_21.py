
def nth_even(n):
  count=0
  for i in range(10000000000):
    if not i%2:
      count+=1
      if count==n:
        return i

