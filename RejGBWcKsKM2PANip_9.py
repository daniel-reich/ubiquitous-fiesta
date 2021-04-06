
def number_syllables(word):
  a = 0
  for i in word:
    if(i == '-'):
      a = a+1
  return a+1

