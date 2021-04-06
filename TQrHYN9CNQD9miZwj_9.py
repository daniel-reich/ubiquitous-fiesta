
def fix_import(s):
  myorder = [2, 3, 0, 1]
  split_mod = s.split(" ")
  return " ".join([split_mod[i] for i in myorder])

