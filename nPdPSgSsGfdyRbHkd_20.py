
def hacker_speak(txt):
  replacements = (("a","4"),("e","3"),("i","1"),("o","0"),("s","5"))
  leeted = txt
  for old, new in replacements:
      leeted = leeted.replace(old, new)
  return leeted

