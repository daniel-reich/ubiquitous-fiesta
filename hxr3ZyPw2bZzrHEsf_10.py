
def make_title(txt):
  new_txt = txt[0].upper()
  for n in range(1, len(txt)):
    if txt[n-1] == ' ':
      new_txt += txt[n].upper()
    else:
      new_txt += txt[n]
  return new_txt

