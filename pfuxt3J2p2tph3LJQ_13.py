
def forbidden_letter(char, lst):
  for word in lst:
    if char in word:
      return False
    else:
      pass
  return True

