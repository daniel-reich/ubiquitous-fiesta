
def ascii_capitalize(txt):
  for char in txt:
    if ord(char) % 2 != 0:
      txt = txt.replace(char, char.lower())
    elif ord(char) % 2 == 0:
      txt = txt.replace(char, char.upper())
  return txt

