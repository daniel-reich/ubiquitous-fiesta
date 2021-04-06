
def to_boolean_list(word):
  return [bool((ord(c)-96)&1) for c in word]

