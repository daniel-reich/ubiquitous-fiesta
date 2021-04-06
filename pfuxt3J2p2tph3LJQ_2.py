
def forbidden_letter(char, lst):
  for i in lst:
    if char in i:
      return False
  return True

