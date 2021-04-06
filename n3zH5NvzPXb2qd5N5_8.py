
def how_mega_is_it(n):
  n=int(abs(n))
  if n<100:return "not a mega milestone"
  else:
    ans="MEGA milestone"
    n=int(abs(n))/10
    while n>=100:
      ans="MEGA "+ans
      n=n/10
    return ans

