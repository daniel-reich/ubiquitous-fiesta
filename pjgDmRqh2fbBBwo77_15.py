
def has_syncopation(s):
  return any(i%2 for i,v in enumerate(s) if v=="#")

