
def blah_blah(txt, n):
  l = txt.split()
  if len(l) < n:
    return " ".join(["blah"]*len(l)) + '...'
  return " ".join(l[:len(l) - n] + ['blah']*n) + "..."

