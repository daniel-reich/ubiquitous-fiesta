
def has_syncopation(s):
  if s == "":
    return False
  for i in range(1,len(s),2):
    if s[i] == "#":
      return True
  return False

