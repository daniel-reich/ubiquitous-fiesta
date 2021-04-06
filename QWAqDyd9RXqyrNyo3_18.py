
def abbreviate(sentence, n=4):
  return "".join([word[0].upper() for word in sentence.split() if len(word) >= n])

