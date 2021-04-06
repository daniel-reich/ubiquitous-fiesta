
def score_it(s):
  level,res,tmp = 0,0,'0'
  for c in s:
    if c.isdigit():
      tmp += c
    else:
      res += level*int(tmp)
      tmp = '0'
      if c == '(':
        level += 1
      elif c == ')':
        level -= 1
  return res

