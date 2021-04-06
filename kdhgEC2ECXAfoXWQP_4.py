
def transpose_matrix(mtx):
  s = ""
  a2 = zip(*mtx)
  for i in list(a2):
    s += " ".join(i) + " "
  return s[0:-1]

