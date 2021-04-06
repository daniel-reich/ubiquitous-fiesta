
def is_strange_pair(txt1, txt2):
  if len(txt1) > 0 and len(txt2) > 0:
    return txt1[0] == txt2[len(txt2) - 1] and txt2[0] == txt1[len(txt1) - 1]
  elif len(txt1) == len(txt2):
    return True
  else:
    return False

