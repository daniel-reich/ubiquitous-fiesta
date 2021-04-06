
def multiply(n1, n2):
  ans = sum(n1 for i in range(abs(n2)))
  return ans if n2 > 0 else -ans

