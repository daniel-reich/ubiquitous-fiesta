
letters = "abc"
def remove_abc(txt):
  a=''.join([i if i not in letters else '' for i in txt])
  if a==txt: return None
  return a

