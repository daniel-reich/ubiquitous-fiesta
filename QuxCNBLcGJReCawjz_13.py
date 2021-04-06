
from math import ceil,floor
def palindrome_type(n):
  s,b = str(n),bin(n)[2:]
  l,r = s[:floor(len(s)/2)],s[ceil(len(s)/2):]
  f,d = b[:floor(len(b)/2)],b[ceil(len(b)/2):]
  rs,bs = (l == r[::-1]), (f == d[::-1])
  if rs == True and bs == True:
    return "Decimal and binary."
  elif rs == True:
    return "Decimal only."
  elif bs == True:
    return "Binary only."
  return "Neither!"

