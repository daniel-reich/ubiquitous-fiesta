
def char_appears(sentence, char):
  #return [word.count(char) for word in sentence.lower().split()]
  return list(map(lambda x: x.count(char), sentence.lower().split()))

