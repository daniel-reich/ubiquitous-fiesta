
alphabet = "abcdefghijklmnopqrstuvwxyz"
def move(word):
  string = ""
  for char in word:
    i = alphabet.index(char)
    string += alphabet[i + 1]
  return string

