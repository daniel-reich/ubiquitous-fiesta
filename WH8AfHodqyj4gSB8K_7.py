
const = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
def is_authentic_skewer(s):
  if s[0] not in const or s[-1] not in const: return False
  d = 0
  for i in range(1, len(s)):
    if s[i].isalpha():
      d = i - 1
      break
  if d == 0: return False
  s = s.split('-' * d)
  for i in range(len(s) - 1):
    if (s[i][0] == '-' or s[i+1][0] == '-') or (s[i] in const and s[i+1] in const): return False
  return True

