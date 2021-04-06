
def is_isomorphic(s, t):
  ss = ''
  tt = ''
  for x in s:
    if x not in ss:
      ss += x
  for x in t:
    if x not in tt:
      tt += x
  if len(ss) != len(tt): return False
  return s.translate(str.maketrans(ss, tt)) == t

