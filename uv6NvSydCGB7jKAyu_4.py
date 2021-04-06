
def is_parsel_tongue(sentence):
  words = sentence.lower().split(" ")
  for i in range(len(words)):
    if "s" in words[i]:
      if not("ss" in words[i]):
        return False
  return True

