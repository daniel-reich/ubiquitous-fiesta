
def persistence(num):
  count = 0
  while(len(str(num))>1):
    prod = 1
    for dig in str(num):
      prod*=int(dig)
    num = prod
    count+=1
  return count

