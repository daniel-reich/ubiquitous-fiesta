
def neutralise(s1, s2):
  return "".join([i if i == j else "0" for i,j in zip([i for i in s1],[i for i in s2])])

