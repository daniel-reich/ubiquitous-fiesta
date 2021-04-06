
def how_mega_is_it(n):
  n = abs(n)
  if n<100:
    return "not a mega milestone"
  ret = ""
  while n>=100:
    ret+="MEGA "
    n/=10
  return ret+"milestone"

