
def min_removals(txt1, txt2):
  t = 0
  for i in txt1+txt2:
    if (txt1+txt2).count(i) == 1:
      t += 1
  return t

