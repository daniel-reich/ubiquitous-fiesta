
def partially_hide(phrase):
  lst = phrase.split(" ")
  new = []
  dash = 0
  for i, val in enumerate(lst):
    if len(val) > 2:
      dash = len(val)-2
    else:
      dash = 0
    new.append(val[0] + "-"*dash + val[-1])
  return " ".join(new)

