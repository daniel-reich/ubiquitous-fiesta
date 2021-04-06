
def blah_blah(txt, n):
  t = txt.split()
  if n >= len(t):
    res = "blah "*(len(t)-1) + "blah..."
    return res
  else:
    i = -1*n
    while i < 0:
      t[i] = "blah"
      i += 1
    return " ".join(t) + "..."

