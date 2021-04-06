
def is_strange_pair(txt1, txt2):
  if len(txt1) == 0 and len(txt2) == 0:
    return True
  if len(txt1) == 0 or len(txt2) == 0:
    return False
  else:
    txt2 = txt2[::-1]
    return True if txt1[0]==txt2[0] and txt1[-1]==txt2[-1] else False

