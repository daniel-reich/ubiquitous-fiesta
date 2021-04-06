
def score_it(s):
  parCount = 0
  finalCount = 0
  i = 0
  while i < len(s):
    if s[i] == '(':
      parCount += 1
    elif s[i] == ')':
      parCount -= 1
    elif s[i].isnumeric():
      bigNum = s[i]
      while s[i + 1].isnumeric():
        bigNum += s[i + 1]
        i += 1
      finalCount += int(bigNum) * parCount
    i += 1
  return finalCount

