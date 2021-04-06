
def partitions(n):
  """
  ALGORITHM:
  Represent n as a string of ones. Count from 0:2^(n-1)-1 in binary,
  letting each bit determine whether to insert a `slice'.
​
  Illustration for n = 4:
  1+1+1+1 = 4
   0 0 0  : 4
   0 0 1  : 3 + 1
   0 1 0  : 2 + 2
   0 1 1  : 2 + 1 + 1
   1 0 0  : 1 + 3
   1 0 1  : 1 + 2 + 1
   1 1 0  : 1 + 1 + 2
   1 1 1  : 1 + 1 + 1 + 1
​
  Order each partition and return number of unique.
  """
  if n == 0: return 1
​
  unique_partitions = set()
  for p in range(2**(n - 1)):
    chunks = []
    chunk = 1
    for i in range(n - 1):
      if (1 << i) & p == 0: # read ith bit
        chunk += 1
      else:
        chunks.append(chunk)
        chunk = 1
    chunks.append(chunk)
    unique_partitions.add(tuple(sorted(chunks)))
  return len(unique_partitions)

