
def validate_spelling(t):
  w = t.split()[-1].strip('.!?')
  return ''.join(t.split('. ')[:len(w)]) == w.upper()

