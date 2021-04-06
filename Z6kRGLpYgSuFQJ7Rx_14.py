
def find_longest(sentence):
  return max(sentence.replace("'"," ").replace('.',' ').lower().split(), key=len)

