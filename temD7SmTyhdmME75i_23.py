
def to_boolean_list(word):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  output = []
  for letter in word:
      if (alphabet.index(letter) + 1) % 2 != 0:
          output.append(True)
      else:
          output.append(False)
  return output

