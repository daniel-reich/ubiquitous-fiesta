
def single_occurrence(txt):
  txt = txt.upper()
  string = ""
  for x in txt:
    if txt.count(x) == 1:
      string += x
  return string

