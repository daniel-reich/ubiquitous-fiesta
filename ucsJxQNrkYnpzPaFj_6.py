
def char_appears(sentence, char):
  sentence=sentence.lower().split()
  return [i.count(char) for i in sentence]

