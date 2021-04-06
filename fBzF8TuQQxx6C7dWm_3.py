
def add(char, txt):
  new_txt = ''
  for i in txt:
    if i == ' ':
      i = char
    new_txt += i
  return new_txt

