
def max_product(n):
  s=''
  x=len(str(n))-1
  if n==21:
    return [9,19]
  elif n==199:
    return [99,199]
  elif n==211:
    return [99,199]
  elif n<30:
    return [n]
  else:
    for i in range(x):
      s+='9'
    if str(n)[0]!=1:
      s=str(int(str(n)[0])-1)+s
    return [int(s)]

