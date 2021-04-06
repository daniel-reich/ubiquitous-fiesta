
def is_kaprekar(n):
  p=str(n**2)
  if len(p)%2==0:
    return int(p[0:len(p)//2])+int(p[len(p)//2:])==n
  elif len(p)==1:
    return int(p)==n
  return int(p[0:len(p)//2])+int(p[len(p)//2:])==n

