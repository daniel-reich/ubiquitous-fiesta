
def is_strange_pair(txt1, txt2):
  return txt1[:1] == txt2[-1:] and txt1[-1:] == txt2[:1]

