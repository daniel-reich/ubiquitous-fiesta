
def to_boolean_list(txt):
  return [True if (ord(i) - 96) % 2 else False for i in txt]

