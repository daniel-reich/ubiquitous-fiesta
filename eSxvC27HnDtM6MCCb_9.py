
def base_n(base, values, num):
  if len(values)!=base:
    return False
  A=[]
  while num:
    A.append(num%base)
    num//=base
  A=A[::-1]
  res=''
  for x in A:
    res+=str(values[x])
  return res

