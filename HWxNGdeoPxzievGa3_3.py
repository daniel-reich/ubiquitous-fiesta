
def is_strange_pair(txt1, txt2):
  if txt1=="" and txt2=="":
    return True
  elif txt1=="" or txt2=="":
    return False
  return txt1[-1]==txt2[0] and txt1[0]==txt2[-1]

