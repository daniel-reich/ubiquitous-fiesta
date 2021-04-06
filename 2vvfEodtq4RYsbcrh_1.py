
def is_safe_bridge(s):
  x = len(s)
  y = s.count("#")
  if x == y:
    return True
  else:
    return False

