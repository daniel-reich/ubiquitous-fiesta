
def is_isogram(txt):
  return max([txt.lower().count(x) for x in txt.lower()]) == 1

