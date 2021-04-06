
def is_ascending(s):
  n=len(s)
  A=[x for x in range(1, n) if n%x==0]
  C=[]
  for x in A:
    B=[int(s[i:i+x]) for i in range(0, n, x)]
    C.append(B)
  return any(list(range(x[0], x[-1]+1))==x for x in C)

