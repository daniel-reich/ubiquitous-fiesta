
def char_appears(sentence, char):
  return [word.count(char.lower()) for word in sentence.lower().split()]

