
def single_occurrence(txt):
  if len(txt) == 0:
    return ''
  txt = txt.upper()
  for i in txt:
    if txt.count(i) == 1:
      return i

