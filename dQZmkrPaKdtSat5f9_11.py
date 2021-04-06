
def single_occurrence(txt):
  txt = txt.upper()
  return [l for l in txt if txt.count(l) == 1][0] if txt else ''

