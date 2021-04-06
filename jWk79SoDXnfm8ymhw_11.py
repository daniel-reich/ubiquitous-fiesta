
def censor(sentence):
  return " ".join(word if len(word)<=4 else "*"*len(word) for word in sentence.split())

