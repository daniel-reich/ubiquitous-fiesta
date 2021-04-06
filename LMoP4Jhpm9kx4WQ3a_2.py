
def is_ascending(s, meh = None):
  if meh is None:
    for idx in range(1, len(s)):
      if is_ascending(s, s[:idx]):
        return True
    return False
  else:
    if s == meh:
      return True
    if s.startswith(meh):
      return is_ascending(s[len(meh):], str(int(meh)+1))
    return False

