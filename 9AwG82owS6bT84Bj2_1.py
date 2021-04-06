
def doubled_pay(n):
  sum = 0
  temp = 1
  for i in range(1,n+1):
    sum += temp
    temp *= 2
  return sum

