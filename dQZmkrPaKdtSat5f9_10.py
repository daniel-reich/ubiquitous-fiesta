
def single_occurrence(txt):
  lst = [x for x in txt.lower() if txt.lower().count(x) == 1]
  return lst[0].upper() if lst else ""

