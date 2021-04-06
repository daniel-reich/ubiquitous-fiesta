
def kaprekar_numbers(p,q,r=''):
  for i in range(p,q+1):
    s=str(i**2)
    d=len(s)//2
    if int(s[:d]or 0)+int(s[d:])==i:r+='%s '%i
  return r[:-1]or'INVALID RANGE'

