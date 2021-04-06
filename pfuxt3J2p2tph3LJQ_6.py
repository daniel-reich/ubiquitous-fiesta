
def forbidden_letter(char, lst):
  for i in lst:
    for element in i:
      if element == char:
        return False
  return True

