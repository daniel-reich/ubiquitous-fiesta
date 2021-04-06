
def validate_spelling(s):
  s = s.lower()[:-1].split('. ')
  for a,b in zip(s[:-1], s[-1]):
    if a != b:
      return False
  return True

