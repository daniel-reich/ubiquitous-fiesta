
def min_removals(txt1, txt2):
  x=len(set(txt1) - set(txt2))
  y=len(set(txt2)-set(txt1))
  return x+y

