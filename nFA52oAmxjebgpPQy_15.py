
def char_index(word, char):
  if char not in word:
    return None
  lst = []
  lst.append(word.index(char))
  lst.append(word.rindex(char))
  return lst

