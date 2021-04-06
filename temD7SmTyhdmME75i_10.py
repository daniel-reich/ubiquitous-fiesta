
def to_boolean_list(word):
  return [bool(" abcdefghijklmnopqrstuvwxyz".index(i)%2) for i in word]

