
def fact_of_fact(n):
  res = 1
  for i in range(1,n+1):
    res*=fact(i)
  return res
​
def fact(n):
  res = 1
  for i in range(1,n+1):
    res*=i
  return res

