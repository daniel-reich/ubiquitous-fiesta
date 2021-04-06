
def not_good_math(n, k):
  x = str(n)
  for i in range(k):
    if x[-1] == '0':  
      x = x[:-1]
    else:
      x = str(int(x) - 1)
  return int(x)

