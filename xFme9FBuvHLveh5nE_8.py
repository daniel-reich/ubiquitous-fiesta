
def is_zygodrome(num):
  num = str(num)
  check = False
  for x,y in zip(num,num[1:]):
    if x!=y and check==False:
      return False
    check = x==y
  return check

