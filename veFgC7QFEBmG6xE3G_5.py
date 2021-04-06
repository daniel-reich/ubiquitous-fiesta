
def is_smooth(sentence):
  i = 0
  L = sentence.split(' ')
  while i < len(L)-1:
    if L[i][-1].lower() == L[i+1][0].lower():
      i+= 1
      continue
    else:
      return False
  return True

