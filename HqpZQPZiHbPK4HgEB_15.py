
def maxmin(n):
  if n==0:
    return (0,0)
  digits=list(str(n))
  digits=list(map(lambda x: int(x),digits))
  digits1=digits.copy()
  for i in range(len(digits)):
    maxd=max(digits[i:])
    if digits[i]!=maxd:
      for j in reversed(range(len(digits))):
        if digits[j]==maxd:
          digits[i],digits[j]=digits[j],digits[i]
          break
      break
  digits=list(map(lambda x: str(x),digits))
  n1=int(''.join(digits))
  print(n1)
  for i in range(len(digits1)):
    print(digits1[i:])
    mind=min(set(digits1[i:])-({0} if i==0 else set()))
    print(mind)
    if digits1[i]!=mind:
      for j in reversed(range(len(digits1))):
        if digits1[j]==mind:
          digits1[i],digits1[j]=digits1[j],digits1[i]
          break
      break
  digits1=list(map(lambda x: str(x),digits1))
  n2=int(''.join(digits1))
  return (n1,n2)

