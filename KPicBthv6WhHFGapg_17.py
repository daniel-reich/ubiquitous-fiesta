
def count_syllables(txt):
  t = txt.lower()
  return t.count(t[0:2])

