
def gen_parts(n,I=1):
  yield (n,)
  for i in range(I, n//2 + 1):
    for p in gen_parts(n-i, i):
      yield (i,) + p
  
def partitions(n):
  return sum(1 for i in gen_parts(n))

