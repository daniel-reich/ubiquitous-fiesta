
def add(char, txt):
  for i in txt:
    if i == " ":
      txt = txt.replace(i, char)
      return txt

