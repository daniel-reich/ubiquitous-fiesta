
def is_smooth(sentence):
  s = sentence.lower().split(' ')
  for x in range(len(s) - 1):
    if s[x][-1] != s[x+1][0]:
      return False
  return True

