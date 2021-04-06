
def to_scottish_screaming(txt):
  lst_vowel = ["a","e","i","o","u"]
  flag = False
  txt = txt.lower()
  for i in txt:
    if i in lst_vowel:
      flag = True
      txt = txt.replace(i,"e")
  if flag:
    return txt.upper()

