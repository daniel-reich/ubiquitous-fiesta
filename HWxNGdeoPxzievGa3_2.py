
def is_strange_pair(txt1, txt2):
  if not txt1 and not txt2: return True
  if not txt1 or not txt2: return False
  return txt1[0] == txt2[-1] and txt1[-1] == txt2[0]

