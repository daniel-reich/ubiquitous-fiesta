
def is_exact(n, i=1):
  fact = lambda x: 1 if x<2 else x*fact(x-1)
  if fact(i)==n:
    return [n,i]
  if fact(i)>n:
    return "Not exact!" 
  return is_exact(n, i+1)

