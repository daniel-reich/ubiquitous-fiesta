
def paul_cipher(txt):
  shift = lambda a, b: chr((ord(a) + ord(b) - 129) % 26 + 65)
  txt = txt.upper()
  res = ""
  prev = ""
  for i in range(len(txt)):
    if txt[i].isalpha():
      res += shift(prev, txt[i]) if prev else txt[i]
      prev = txt[i]
    else:
      res += txt[i]
  return res

