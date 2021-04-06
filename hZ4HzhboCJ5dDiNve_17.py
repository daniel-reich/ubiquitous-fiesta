
def special_reverse_string(txt):
  txt1 = txt.replace(' ', '')[::-1]
  txt2 = list(txt)
  for i in range(len(txt2)):
    if txt[i] != ' ':
      if txt[i].isupper():
        txt2[i] = txt1[0].upper()
      else:
        txt2[i] = txt1[0].lower()
      txt1 = txt1[1:]
  return ''.join(txt2)

