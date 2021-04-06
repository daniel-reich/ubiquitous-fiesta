
def not_good_math(n, k):
  if k == 0:
    return n
  elif str(n)[-1] == '0':
    n = int(str(n)[:-1])
    k -= 1
  else:
    n -= 1
    k -= 1
  
  return not_good_math(n, k)

