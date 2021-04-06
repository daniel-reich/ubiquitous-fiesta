
def alphanumeric_restriction(s):
  for i in s:
    if s.isalpha():
      return True
    elif s.isdigit():
      return True
 
  return False

