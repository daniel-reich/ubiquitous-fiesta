
def paul_cipher(txt):
  prev = None
  fin = ''
  for char in txt:
    if char.isalpha():
      new = ord(char.upper())-65
      if prev:
        new+=ord(prev)-64
      prev = char.upper()
      fin+=chr((new%26)+65)
    else:
      fin+=char
  return fin

