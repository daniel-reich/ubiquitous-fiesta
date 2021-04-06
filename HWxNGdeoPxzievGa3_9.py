
def is_strange_pair(txt1, txt2):
  if txt1 == txt2 == "": return True
  try:
    return txt1[0] == txt2[-1] and txt2[0] == txt1[-1]
  except:
    return False

