
def eng2nums(s):
  u = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
  d = {2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
  ex = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
  ru = {v:k for k,v in u.items()}
  ru['']=1
  rd = {v:k*10 for k,v in d.items()}
  rex = {v:k for k,v in ex.items()}
  meh = {}
  meh.update(ru)
  meh.update(rd)
  meh.update(rex)
  hs = 0
  if 'hundred' in s:
    h, s = [r.strip() for r in s.split('hundred')]
    hs = ru[h]*100
  return hs + (sum(meh[p] for p in s.split(' ')) if s else 0)

