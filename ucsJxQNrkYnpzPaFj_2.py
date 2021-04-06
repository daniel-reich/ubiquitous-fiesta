
def char_appears(sentence, char):
  arr = sentence.lower().split()
  return [x.count(char.lower()) for x in arr]

