
def is_smooth(sentence):
  s=sentence.split(' ')
  for i in range(0,len(s)-1):
    if((s[i][-1]).lower()!=(s[i+1][0]).lower()):
      return False
  return True

