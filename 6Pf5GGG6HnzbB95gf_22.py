
def find_factors(n):
  if n >= 1:
    ans = [i for i in range(1, n+1) if n % i == 0]
  else:
    ans = []
  return ans

