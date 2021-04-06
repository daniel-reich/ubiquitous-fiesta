
def can_alternate(s):
  return True if abs(s.count("0") - s.count("1")) < 2 else False

