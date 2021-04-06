
def single_occurrence(txt):
  return min(txt.upper(), key = txt.upper().count) if txt else ''

