
def is_parsel_tongue(sentence):
  words = sentence.lower().split()
  if all("ss" in word or "s" not in word for word in words): return True
  return False

