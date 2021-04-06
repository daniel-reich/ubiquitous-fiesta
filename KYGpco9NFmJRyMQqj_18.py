
def min_removals(txt1, txt2):
  f = len([i for i in txt1 if i not in txt2])
  s = len([i for i in txt2 if i not in txt1])
  return (f + s)

