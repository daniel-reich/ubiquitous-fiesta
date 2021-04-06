
def count_syllables(txt):
  txt = txt.lower()
  return txt.count(txt[:2])

