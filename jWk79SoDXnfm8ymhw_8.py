
def censor(s):
  return ' '.join(len(w)*'*' if len(w) > 4 else w for w in s.split())

