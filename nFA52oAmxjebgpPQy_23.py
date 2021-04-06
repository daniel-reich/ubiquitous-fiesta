
def char_index(word, char):
  return [word.index(char), word.rindex(char)] if char in word else None

