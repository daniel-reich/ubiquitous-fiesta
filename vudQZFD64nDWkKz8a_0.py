
def grant_the_hint(txt):
  words = txt.split()
  m = max(len(w) for w in words) + 1
  return [' '.join(w[:i] + '_'*(len(w)-i) for w in words) for i in range(m)]

