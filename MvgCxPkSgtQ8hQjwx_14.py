
def remove_vowels(txt):
  s = "ueoaiUEOAI"
  for i in txt:
    if i in s:
      txt = txt.replace(i,"")
  return txt

