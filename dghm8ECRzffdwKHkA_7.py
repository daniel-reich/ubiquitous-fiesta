
def capital_letters(txt):
  capitalized = 0
  for i in txt:
    if i.isupper() == True:
      capitalized += 1
  return capitalized

