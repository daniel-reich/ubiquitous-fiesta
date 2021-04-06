
def char_index(word, char):
  for x in range(len(word)):
    if char not in word:
      return None
    elif word[x] == char:
      return [x, word.rindex(char)]

