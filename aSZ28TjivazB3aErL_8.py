
def letters_only(s):
  if len(s) < 1:
    return False
  for i in range(0,len(s)):
    if s[i].islower() or s[i] == " ":
      continue
    else:
      return False
  return True

