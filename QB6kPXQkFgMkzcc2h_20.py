
def remove_abc(txt):
  letterA = "a"
  letterB = "b"
  letterC = "c"
  if letterA or letterB or letterC in txt :
    newStringa = txt.replace('a', '')
    newStringb = newStringa.replace('b','')
    newStringc = newStringb.replace('c', '')
    if newStringc == txt:
      return None
    else :
      return newStringc

