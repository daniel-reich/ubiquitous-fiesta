
def persistence(num, p = 0):
  if num < 10: return p
  return persistence(eval('*'.join(str(num))), p+1)

