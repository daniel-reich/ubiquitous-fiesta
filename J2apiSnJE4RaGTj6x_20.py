
def find_broken_keys(txt1, txt2):
  a = []
  for i, x in enumerate(txt1):
    if txt2[i] != x and x not in a:
      a.append(x)
  return a

