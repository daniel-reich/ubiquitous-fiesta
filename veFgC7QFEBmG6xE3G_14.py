
def is_smooth(sentence):
  sentence=sentence.split()
  for i in range(len(sentence)-1):
    if sentence[i][-1].lower()!=sentence[i+1][0].lower(): return False
  return True

