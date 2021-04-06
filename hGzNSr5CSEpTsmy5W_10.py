
def not_good_math(n, k):
  if k == 0:
    return n
  if not n%10:
    n//=10
  else:
    n -= 1
  return not_good_math(n,k-1)

