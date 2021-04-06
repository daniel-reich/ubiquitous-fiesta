
def to_boolean_list(s):
  return [bool(ord(c)-96 & 1) for c in s]

