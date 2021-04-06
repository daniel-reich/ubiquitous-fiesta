
def count_syllables(txt):
  txt = txt.lower()
  syl = 0 
  for i in txt:
    if i in "aeiou":
      syl += 1
  return syl

