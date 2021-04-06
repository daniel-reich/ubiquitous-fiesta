
def char_appears(sentence, char):
  return [i.count(char) for i in sentence.lower().split()]

