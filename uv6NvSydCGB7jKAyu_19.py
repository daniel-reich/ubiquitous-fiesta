
def is_parsel_tongue(sentence):
  words = sentence.split(" ")
  s_words = [word.lower() for word in words if "s" in word.lower()]
  test = True
  
  for word in s_words:
    if "ss" not in word:
      test = False
  
  return test

