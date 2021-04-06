
def is_safe_bridge(s):
  for x in s:
    if x != '#':
      return False
  return True

