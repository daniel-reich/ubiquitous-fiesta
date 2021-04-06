
def forbidden_letter(char, lst):
  return len([el for el in lst if el.count(char) == 0]) == len(lst)

