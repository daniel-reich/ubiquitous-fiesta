
def forbidden_letter(char, lst):
  return not any(char in x for x in lst)

