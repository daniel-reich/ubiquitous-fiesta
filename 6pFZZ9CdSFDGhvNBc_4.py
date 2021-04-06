
def factor_group(num):
  return "even" if sum([num%x==0 for x in range(1,num+1)])%2==0 else "odd"

