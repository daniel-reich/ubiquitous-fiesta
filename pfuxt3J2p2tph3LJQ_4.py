
def forbidden_letter(char, lst):
  return all(char not in word for word in lst)

