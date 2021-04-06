
def can_alternate(s):
  if s.count("1") == s.count("0"):
    return True
  if s.count("1") == s.count("0") + 1:
    return True
  if s.count("0") == s.count("1") + 1:
    return True
  else:
    return False

