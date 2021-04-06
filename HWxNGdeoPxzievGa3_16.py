
def is_strange_pair(txt1, txt2):
  if txt1 == txt2:
    return True
  elif txt1 == '' and len(txt2)> 0:
    return False
  return txt1[0] == txt2[-1] and txt1[-1] == txt2[0]

