
def is_kaprekar(n):
  num = str(n**2)
  if len(num)>1:
    n1 = int(num[:len(num)//2])
    n2 = int(num[len(num)//2:])
  else:
    n1=int(num)
    n2=0
  return n1+n2==n

