
def is_strange_pair(txt1, txt2):
  if (txt1 == "" or txt2 ==""): return txt1 == txt2
  else: return txt1[0] == txt2[-1] and txt1[-1] == txt2[0]

