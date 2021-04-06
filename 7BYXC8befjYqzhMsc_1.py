
def classify_rug(pattern):
  if all(i == i[::-1] for i in pattern):
    if all(pattern[i] == pattern[-(1+i)] for i in range(len(pattern))): 
      return 'perfect'
    return 'vertically symmetric'
  elif all(pattern[i] == pattern[-(1+i)] for i in range(len(pattern))):
    return 'horizontally symmetric'
  return 'imperfect'

