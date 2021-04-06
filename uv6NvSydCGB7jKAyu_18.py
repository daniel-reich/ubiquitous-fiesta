
def is_parsel_tongue(sentence):
  words = [w for w in sentence.lower().split() if 's' in w]
  return all(w.find('ss') != -1 for w in words)

