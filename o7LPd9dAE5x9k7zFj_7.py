
def logarithm(base, num):
  x=0
  if num==1:
    return 0
  if base<=1 or num<1:
    return "Invalid"
  while base<=num:
    x+=1
    num=num/base
  return x

