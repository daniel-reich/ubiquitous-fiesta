
def min_removals(txt1, txt2):
  txt1,txt2 = set(txt1),set(txt2)
  diff = len(txt1-txt2) + len(txt2-txt1)
  return diff

