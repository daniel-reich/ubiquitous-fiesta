
def char_index(word, char):
  if char not in word:
    return None
  else:
    return [word.index(char), len(word)-1-word[::-1].index(char)]

