
def num_type(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum+=i
  sum1=0
  for i in range(1,sum):
    if sum%i==0:
      sum1+=i
  if sum==n:
    return "Perfect"
  elif n==sum1:
    return "Amicable"
  else:
    return "Neither"

