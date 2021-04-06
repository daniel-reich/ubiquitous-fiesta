
def prime_numbers(num):
  if num<2:
    return 0
  else:
    c=2
    ans=0
    while True:
      m = 0
      for x in range(c//2,1,-1):
        if c%x==0:
          m=1
          break
      if not m:
        ans+=1
      if c<num:
        c+=1
      else:
        break
    return ans

