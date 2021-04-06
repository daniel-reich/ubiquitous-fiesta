
def is_consecutive(s, asc = None, meh = None):
  if meh is None:
    for idx in range(1, len(s)):
      if is_consecutive(s, True, s[:idx]) or is_consecutive(s, False, s[:idx]):
        return True
    return False
  else:
    if s == meh:
      return True
    if s.startswith(meh):
      if asc:
        return is_consecutive(s[len(meh):], asc, str(int(meh)+1))
      else:
        return is_consecutive(s[len(meh):], asc, str(int(meh)-1))
    return False

