
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return "".join([alphabet[(alphabet.index(i) + key) % 26] if i.isalpha() else " " for i in text])

