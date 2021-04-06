
def char_index(word, char):
  if char not in word:
    return None
  return [word.find(char),word.rfind(char)]

