
def is_strange_pair(txt1, txt2):
  if txt1 == "" and txt2 == "":
    return True
  if (txt1 == "" and txt2 != "") or (txt2 == "" and txt1 != ""):
    return False
  return txt1[0] == txt2[-1] and txt2[0] == txt1[-1]

