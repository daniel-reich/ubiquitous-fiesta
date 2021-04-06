
def not_good_math(n,k):
  while k > 0:
      if n%10==0:
          n //= 10
      else:
          n -= 1
      k -= 1
  return n

