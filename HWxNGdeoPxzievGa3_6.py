
def is_strange_pair(txt1, txt2):
  try:
    return True if (txt1 == "" and txt2 == "") or (txt1[0]== txt2[-1] and txt1[-1] == txt2[0]) else False
  except:
    return False

