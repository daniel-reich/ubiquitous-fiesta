
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  a =  ""
  for i in range(len(text)):
    if text[i] == " ":
      a += " "
    elif text[i] != " ":
            a += alphabet[alphabet.index(text[i]) + key]
  return a

