
def prime(x):
  return x > 1 and not any (x%i==0 for i in range (2,x))
​
def left(x):
  return all(prime(int(x[i:])) for i in range (len(x)))
​
def right(x):
  return all(prime(int(x[:i+1])) for i in range (len(x)))
​
def truncatable(n):
  n = str(n)
  if "0" in n:
    return False
  if left(n) and right(n):
    return "both"
  if left(n):
    return "left"
  if right(n):
    return "right"
  else:
    return False

