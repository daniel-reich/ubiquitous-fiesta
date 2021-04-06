
def char_index(word, char):
  try:
    res = [word.index(char), word.rindex(char)]
  except:
    res = None
  return res

