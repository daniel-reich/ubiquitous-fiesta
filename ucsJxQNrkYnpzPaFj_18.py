
def char_appears(sentence, char):
  appearance = []
  for word in sentence.lower().split():
    appearance.append(word.count(char))
  return appearance

