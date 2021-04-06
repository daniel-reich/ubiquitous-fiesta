
def alphanumeric_restriction(s):
  return (all(i.isnumeric() for i in s) or all(i.isalpha() for i in s)) if s else False

