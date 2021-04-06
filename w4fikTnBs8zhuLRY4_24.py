
def rep_set(n, x=[]):
  lst=[]
  for _ in range(n):
      lst.append(x)
      x = (x or []) + [x]
  return lst

