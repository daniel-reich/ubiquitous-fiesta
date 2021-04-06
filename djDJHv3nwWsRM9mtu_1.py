
def validate_spelling(t):
  l=t.split('. ')
  return''.join(l[:-1])==(l[-1].upper()[:-1])

