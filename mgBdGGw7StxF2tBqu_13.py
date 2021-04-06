
def duplicates(txt):
  txt = [i for i in txt if txt.count(i) > 1]
  return len(txt) - len(set(txt))

