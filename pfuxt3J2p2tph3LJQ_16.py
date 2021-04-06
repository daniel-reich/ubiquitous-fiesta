
def forbidden_letter(char, lst):
  if lst == []:
    return True
  for x in lst:
    if char in x:
      return False
  return True

