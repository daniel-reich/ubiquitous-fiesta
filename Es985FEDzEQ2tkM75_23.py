
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return "".join([alphabet[((alphabet.find(char) + key) % 26)] if char.isalpha() else char for char in text])

