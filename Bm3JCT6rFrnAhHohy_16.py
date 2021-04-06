
def alphabet_index(txt):
  temp = ''
  txt = txt.lower()
  for item in txt:
    if 97 <= ord(item) <= 122:
      temp += str(ord(item)-96)+' '
  return temp[:-1]

