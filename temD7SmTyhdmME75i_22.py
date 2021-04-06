
def to_boolean_list(word):
  v = [(ord(i)-96) %2 for i in word]
  return v

