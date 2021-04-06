
def gen_values(n, i):
  l=[0]
  k=0
  for c in range(int(n/i)):
    k+=i
    l+=[round(k,2)]
  return l

