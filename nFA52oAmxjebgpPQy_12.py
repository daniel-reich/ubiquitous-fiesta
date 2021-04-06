
def char_index(word, char):
  if char not in word:
    return None
  else:
    return [word.index(char), word.rindex(char)]

