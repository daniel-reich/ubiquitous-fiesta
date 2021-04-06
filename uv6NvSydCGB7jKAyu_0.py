
def is_parsel_tongue(sentence):
  return all('ss' in word or 's' not in word for word in sentence.lower().split())

