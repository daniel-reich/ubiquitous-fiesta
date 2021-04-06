
def GCD(lst):
  divisors = []
  i=1
  while i<max(lst)/2:
    if max(lst)%i==0:
      divisors.append(i)
    i=i+1
  divisors2 = []
  for y in divisors:
    for x in lst:
      if x%y==0:
        divisors2.append(y)
  current_amount = 0
  for x in divisors:
    new_amount = divisors2.count(x)
    if new_amount >= current_amount:
      current_amount = new_amount
      i = x
  return i

