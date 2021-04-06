
def is_polydivisible(n):
  return all(int(str(n)[:i+1])%(i+1)==0 for i in range(len(str(n))))

