
def divisor_sum(n):
  return sum(i for i in range (1,1+n//2) if n%i==0)
​
def num_type(n):
  x = divisor_sum(n)
  if x==n:
    return "Perfect"
  if divisor_sum(x)==n:
    return "Amicable"
  return "Neither"

