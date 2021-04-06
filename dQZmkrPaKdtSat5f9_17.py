
def single_occurrence(txt):
  return "".join(x for x in txt.upper() if txt.upper().count(x) == 1)

