
def sharedLetters(a, b):
  txt = ""
  for c in a.lower():
    if c in b.lower():
      if c not in txt:
        txt += c
  
  return ''.join(sorted(txt))

