
def aux(num):
  if not int(num/10):
    return num%10
  return num%10*aux(int(num/10))
​
def persistence(num):
  return 1+persistence(aux(num)) if int(num / 10) else 0

