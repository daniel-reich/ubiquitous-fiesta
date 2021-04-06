
def num_type(x):
  divisors = [i for i in range(1, x) if not x % i]
  if sum(divisors) == x:
    return("Perfect")
​
  y = sum(divisors)
  y_divisors = [i for i in range(1, y) if not y % i]
  if sum(y_divisors) == x:
    return("Amicable")
  else:
    return("Neither")

