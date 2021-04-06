
def has_syncopation(s):
  return any(1 if i%2 and x=="#" else 0 for i,x in enumerate(s))

