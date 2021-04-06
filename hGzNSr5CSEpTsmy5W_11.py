
def not_good_math(n, k):
  for i in range(k):
    if str(n)[-1] == '0':
      n = int(str(n)[:-1])
    else:
      n -= 1
  return n

