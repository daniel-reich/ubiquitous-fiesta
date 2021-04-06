
def mystery_func(num):
  ans, p = "", 2
  while p<num:
    ans+= "2"
    p*=2
  ans+= str(num-p//2)
  return int(ans)

