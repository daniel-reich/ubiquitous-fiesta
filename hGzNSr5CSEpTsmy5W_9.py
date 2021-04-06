
def not_good_math(n,k):
  for _ in range(k):
    if str(n)[-1]=="0":  n //= 10
    else:  n -= 1
  return n

