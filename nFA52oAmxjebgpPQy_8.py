
def char_index(word, char):
  if char not in word:
    return None
  return [word.find(char),len(word)-1-word[::-1].find(char)]

