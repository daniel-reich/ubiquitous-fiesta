
def single_occurrence(txt):
  if txt == '':
    return ''
  for t in txt:
    if txt.lower().count(t.lower()) == 1:
      return t.upper()

