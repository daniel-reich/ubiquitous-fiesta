
def caesar_cipher(text, key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  out = ''
  for letter in text:
    out += ' ' if letter == ' ' else alphabet[(alphabet.find(letter) + key) % 26]
  return out

