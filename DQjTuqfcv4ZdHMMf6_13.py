
def kaprekar(num):
  def iter(n):
    ns = str(n)+"0"*(4-len(str(n)))
    return int("".join(sorted(ns)[::-1])) - int("".join(sorted(ns)))
  
  c=0
  while num!=6174: 
    num = iter(num)
    c+=1
  return c

