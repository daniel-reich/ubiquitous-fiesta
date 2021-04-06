
def is_parsel_tongue(sentence):
  return all("ss" in i or "s" not in i for i in sentence.lower().split())

