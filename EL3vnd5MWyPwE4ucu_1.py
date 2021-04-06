
def fibonacci(n):
  if n == 0:
    return '0'
  elif n == 1:
    return '1'
  else:
    t2 = 0
    t1 = 1
​
    for i in range(2,n+1):
      total = t1+t2
      t2 = t1
      t1 = total
​
  return "{}".format(total)

