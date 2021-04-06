
def can_build(txt1, txt2):
  need_cs = {}
  for c in txt1:
    need_cs.setdefault(c, 0)
    need_cs[c] += 1
  
  if ' ' in need_cs.keys():
    del need_cs[' ']
    
  for char in need_cs.keys():
    n_av = txt2.count(char)
    if n_av == 0:
      return False
    elif need_cs[char] > n_av:
      #if char != ' ':
      return False
  '''
  for c in txt2:
    need_cs.setdefault(c, 0)
    n_char = txt2.count(c)
    if need_cs[c] == 0 or n_char < need_cs[c]:
      return False
  '''
  return True

