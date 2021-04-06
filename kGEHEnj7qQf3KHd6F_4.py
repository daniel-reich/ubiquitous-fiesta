
def alphanumeric_restriction(s):
  if not s: return False
  return all(d.isdigit() for d in s) or all(c.isalpha() for c in s)

