
import math
def binomial(n,k):
  top = math.factorial(n)
  bottom = math.factorial(k)*math.factorial(n-k)
  return top/bottom
def stirling(n,k):
  sum = 0
  for i in range(0,k+1):
    sum+=math.pow(-1,i)*binomial(k,i)*math.pow(k-i,n)
  return 1/math.factorial(k)*sum
def bell(n):
  sum = 0
  for k in range(0,n+1):
    sum+=stirling(n,k)
  return int(sum)

