
def forbidden_letter(char, lst):
  return not lst or all(char not in w for w in lst)

