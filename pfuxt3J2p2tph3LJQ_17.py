
def forbidden_letter(char, lst):
  return all(list(char not in x for x in lst))

