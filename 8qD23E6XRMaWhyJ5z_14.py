
def happiness_number(s):
  count = 0
  for i in range(len(s)):
    face = s[i:i + 2]
    if face == ':)' or face == '(:':
      count = count + 1
    if face == ':(' or face == '):':
      count = count - 1
  return count

