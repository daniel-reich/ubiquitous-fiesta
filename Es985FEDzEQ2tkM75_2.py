
def caesar_cipher(text, key):
  return ''.join(
    chr((ord(i) - 97 + key) % 26 + 97) if i != ' ' else ' '
    for i in text
  )

