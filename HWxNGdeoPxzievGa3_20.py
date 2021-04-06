
def is_strange_pair(txt1, txt2):
  if not txt1 and txt2:
    return False
  elif not txt1 and not txt2:
    return True
  else:
    return str(txt1[0]) == str(txt2[-1]) and str(txt1[-1]) == str(txt2[0])

