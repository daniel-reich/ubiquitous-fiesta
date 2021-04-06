
def min_removals(txt1, txt2):
  return len(txt1)+len(txt2)-len([x for x in txt1 if x in txt2])*2

