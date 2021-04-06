
def is_parsel_tongue(sentence):
  return all([False for word in sentence.split(" ") if "s" in word.lower() and "ss" not in word.lower()])

