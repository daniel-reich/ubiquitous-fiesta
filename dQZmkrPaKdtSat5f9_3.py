
def single_occurrence(txt): 
  words = [i for i in txt.upper() if txt.upper().count(i) == 1]
  if words:
    return words[0]
  return ''

