
def letters_only(txt):
  return ''.join([x for x in txt if ord(x) in range(65,91) or ord(x) in range(97,123)])

