
def caesar_cipher(text, key):
  abc = "abcdefghijklmnopqrstuvwxyz"
  return ''.join(abc[(key + abc.index(c))%26] if c.isalpha() else c for c in text)

