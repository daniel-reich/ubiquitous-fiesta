
def has_syncopation(s):
  length = len(s)
  if length <= 1:
    return False
  if length <= 3:
    return s[1] == "#"
  if length >= 4:
    if s[1] == "#" and s[3] == "#":
      return True
    index = 5
    while index < length:
      if s[index] == "#":
        return True
      index += 2
    return False

