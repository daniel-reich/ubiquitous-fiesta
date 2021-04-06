
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_word = ""
  for char in text:
    if char == " ":
      new_word += char
    elif (ord(char) + key) <= 122:
      new_word += chr(ord(char) + key)
    else:
      new_word += chr(ord(char) + key - 26)
  return new_word

