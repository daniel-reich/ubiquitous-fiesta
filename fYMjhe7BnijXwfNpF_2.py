
def stmid(txt):
  return ''.join(w[0] if not len(w)%2 else w[len(w)//2] for w in txt.split())

