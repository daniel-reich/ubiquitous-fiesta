
def doubleton(n):
  n+=1
  while len(set([i for i in str(n)]))!=2:
    n+=1
  return n

