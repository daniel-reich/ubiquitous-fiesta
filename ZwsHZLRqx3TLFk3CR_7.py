
def f(x):
  r=1
  for i in range(2,int(x[:-1])+1):
    r*=i
  return r
​
def eval_factorial(lst):
  return sum(map(f,lst))

