
def newton_raphson(lst):
  x = [0.0, 0.0]
  
  for i in range(20):
    x[1] = x[0] - 1.0 * f(lst,x[0]) / (dfdx(lst,x[0]) + 0.0)
    x[0] = x[1]
  
  return(round(x[0],3))
  
def f(lst,x):
  return (lst[0] * x ** 3 + lst[1] * x ** 2 + lst[2] * x + lst[3])
​
def dfdx(lst,x):
  return (3 * lst[0] * x ** 2 + 2 * lst[1] * x + lst[2])

