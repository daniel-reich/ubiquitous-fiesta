
def to_boolean_list(word):
  return [bool(ord(letter) % 2) for letter in word]

