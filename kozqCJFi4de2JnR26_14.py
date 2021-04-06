
def fib_str(n, txt):
  M = [txt[i] if i < 2 else '' for i in range(n)]
  for i in range(2,n):
    M[i] = M[i-1] + M[i-2]
  return ', '.join(M)

