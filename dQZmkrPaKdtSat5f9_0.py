
def single_occurrence(txt):  
  return "".join([i for i in txt.upper() if txt.upper().count(i) == 1])

