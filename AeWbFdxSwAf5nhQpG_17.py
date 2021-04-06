
from functools import reduce 
def persistence(n):
  count = 0
  while len(str(n)) != 1:
    n = reduce(lambda x, y: int(x) * int(y), str(n))
    print(n)
    count += 1
  return (count)

