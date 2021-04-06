
def fact_of_fact(n):
  ans = 1
  for i in range(2, n + 1):
    ans *= i ** ((n + 1) - i)
  return ans

