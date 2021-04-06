
def sum_round(num):
  f,res = 1,[]  
  while num:
    num,r = divmod(num,10)
    r*=f    
    f*=10
    if r != 0:
      res.append(r)
  return ' '.join(map(str,res))

