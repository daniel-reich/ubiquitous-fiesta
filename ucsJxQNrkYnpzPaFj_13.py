
def char_appears(sentence, char):
  return [x.count(char) for x in sentence.lower().split()]

