
def count_syllables(txt):
  if txt.islower():
    return txt.count(txt[0:2])
  elif txt.isupper():
    return txt.count(txt[0:2])
  else:
    txt = txt.lower()
    return txt.count(txt[0:2])

