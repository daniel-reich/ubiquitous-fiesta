
def single_occurrence(txt): 
  txt = txt.upper()
  return '' if not txt else \
    min(txt, key=lambda x: txt.count(x))

