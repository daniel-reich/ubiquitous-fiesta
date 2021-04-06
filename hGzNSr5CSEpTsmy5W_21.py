
def not_good_math(n, k):
  if k:
    a = n-1 if n%10 else n//10
    return not_good_math(a,k-1)
  else:
    return n

