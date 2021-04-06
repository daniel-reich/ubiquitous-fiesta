
def neighboring(txt):
  return all(ord(b) == ord(a)-1 or ord(b) == ord(a)+1 for a,b in zip(txt,txt[1:]))

