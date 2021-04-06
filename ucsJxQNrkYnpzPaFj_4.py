
def char_appears(sentence, char):
  return [i.lower().count(char) for i in sentence.split(' ')]

