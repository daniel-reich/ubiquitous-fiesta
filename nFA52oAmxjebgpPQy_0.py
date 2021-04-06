
def char_index(word, char):
  return None if char not in word else [word.index(char), word.rindex(char)]

