
def to_boolean_list(word):
  return [(ord(elem) -96) % 2 != 0 for elem in word]

