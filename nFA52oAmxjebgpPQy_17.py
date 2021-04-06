
def char_index(word, char):
  if word.find(char)!=-1:
    return [word.find(char),word.rfind(char)]

