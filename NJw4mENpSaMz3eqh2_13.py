
def is_undulating(n):
  n = str(n)
  if len(n)<3 or len(set(n))!=2:
    return False
  a, b = n[0],n[1]
  return all(a==n[i] for i in range(0,len(n),+2)) and all(b==n[i] for i in range(1,len(n),+2))

