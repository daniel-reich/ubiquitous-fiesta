
def single_occurrence(txt):
  for i in set(txt.lower()):
    if txt.lower().count(i) == 1:
      return i.upper()
  return ''

