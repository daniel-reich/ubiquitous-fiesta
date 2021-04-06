
def is_strange_pair(txt1, txt2):
  if txt1 != "" and txt2 != "": 
    if txt1[0] == txt2[-1] and txt1[-1] == txt2[0]:
      return True
    else:
      return False
  elif txt1 == txt2:
    return True
  else:
    return False

