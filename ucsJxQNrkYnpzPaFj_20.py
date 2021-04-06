
def char_appears(sentence, char):
  return [x.lower().count(char) for x in sentence.split()]

