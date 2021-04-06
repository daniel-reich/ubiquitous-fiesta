
def to_boolean_list(word):
  return [bool(ord(i)%2) for i in word]

