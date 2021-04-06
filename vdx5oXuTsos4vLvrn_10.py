
def kaprekar_numbers(p, q):
  res=[]
  for i in range(p,q+1):
    k=len(str(i))
    s=str(i**2)
    left=s[:-k]
    right=s[-k:]
    if not left:
      left='0'
    if int(left)+int(right)==i:
      res.append(str(i))
  return ' '.join(res) if res else 'INVALID RANGE'

