
def vigenere(text, keyword):
  if ' ' in text:
    return encrypt(''.join(x.upper() for y in text.split() for x in y if x.isalpha()), keyword.upper())
  else:
    return decrypt(text, keyword.upper())
​
def encrypt(text, key):
  blocks = to_blocks(text, len(key))
  cipher = []
  for i in blocks:
    s = ''
    for x, y in zip(list(i), list(key)):
      s += chr((((ord(x) - 65) + (ord(y) - 65)) % 26) + 65)
    cipher.append(s)
  return ''.join(x for x in cipher)
​
def decrypt(cipher, key):
  blocks = to_blocks(cipher, len(key))
  msg = []
  for i in blocks:
    s = ''
    for x, y in zip(list(i), list(key)):
      s += chr((((ord(x) - 65) - (ord(y) - 65)) % 26) + 65)
    msg.append(s)
  return ''.join(x for x in msg)
​
def to_blocks(text, length):
  return [text[i:(i+length)] for i in range(0, len(text), length)]

