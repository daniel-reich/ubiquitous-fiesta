
def has_syncopation(s):
  if len(s) < 2:
    return False
  for x in range(1, len(s) + 1, 2):
    if s[x] == "#":
      return True
  return False

