
def single_occurrence(txt):
  return ''.join([i.upper() for i in txt if (txt.lower()).count(i.lower())==1])

