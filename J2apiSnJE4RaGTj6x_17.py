
def find_broken_keys(txt1, txt2):
  
  ret = []
  
  for a, b in zip(txt1, txt2):
    if a != b and a not in ret:
      ret.append(a)
  
  return ret

