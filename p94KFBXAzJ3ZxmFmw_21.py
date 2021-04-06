
def ascii_capitalize(txt):
  new_txt = ""
  for i in txt:
    if ord(i) % 2 == 0: i = i.upper()
    else : i = i.lower()
    new_txt += i
  return new_txt

