
def min_removals(txt1, txt2):
  return sum([1 for i in txt1 if i not in txt2]) + sum([1 for i in txt2 if i not in txt1])

