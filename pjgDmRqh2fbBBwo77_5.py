
def has_syncopation(s):
  for i in range(len(s)):
    if i % 2 == 1 and s[i] == '#':
      return True
  return False

