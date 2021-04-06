
def has_syncopation(s):
  if len(s) < 2:
    return False
  for i in range(len(s)):
    if s[i+1] == "#" or s.count("#") >= 4:
      return True
    else:
      return False

