
def multiply_by_11(n):
  n += '0'
  res = [0,int(n[0])]
  for a,b in zip(n,n[1:]):
    cry,nxt = divmod(int(a)+int(b),10)
    i = -1
    while cry:
      cry,res[i] = divmod(cry+res[i],10)
      i-=1
    res.append(nxt)
  return ''.join(map(str,res[1:] if res[0] == 0 else res))

