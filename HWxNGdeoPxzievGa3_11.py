
def is_strange_pair(txt1, txt2):
​
  if len(txt1) > 0 and len(txt2) > 0:
    if(txt1[0] == txt2[-1] and txt2[0] == txt1[-1]):
      return True
  if len(txt1) == 0 and len(txt2) == 0:
    return True
  return False

