
def alphanumeric_restriction(s):
  if all(x.isalnum() for x in s):
    return len(set(x.isalpha() for x in s)) == 1
  else: return False

