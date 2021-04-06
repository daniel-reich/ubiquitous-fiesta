
def score_it(st):
  ans = 0
  lev = 0
  curr = ''
  for s in st:
    if s in'()':
      ans += int(curr)*lev if curr else 0
      curr = ''
      if s == '(': lev+=1
      else: lev-=1
    elif s.isnumeric():
      curr+= s
  ans += int(curr) if curr*lev else 0
  return ans

