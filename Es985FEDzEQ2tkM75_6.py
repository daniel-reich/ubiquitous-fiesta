
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  res = ''
  for x in text:
    if x!=' ':
      res+=alphabet[(alphabet.index(x)+ key)%26]
    else:
      res+= ' '
  return res

