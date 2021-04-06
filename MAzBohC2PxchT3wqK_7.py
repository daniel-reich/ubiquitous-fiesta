
def shadow_sentence(a, b):
  if len(a.split())!=len(b.split()):
    return False
  for i,j in zip(a.split(),b.split()):
    if len(i)!=len(j):
      return False
    i = set(i)
    j = set(j)
    if len(i.union(j))!=len(i)+len(j):
      return False
  return True

