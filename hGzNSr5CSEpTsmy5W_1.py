
def not_good_math(n,k):
  for a in range(k):
    if n%10==0:
      n/=10
    else:
      n-=1
  return n
