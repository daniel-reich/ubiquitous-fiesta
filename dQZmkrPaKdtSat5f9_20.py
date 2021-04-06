
def single_occurrence(txt):
  txt = txt.lower()
  for i in txt:
    if txt.count(i) == 1: return i.upper()
  return ''

