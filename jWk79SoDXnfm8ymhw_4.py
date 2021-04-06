
def censor(s):
  return " ".join([word if len(word)< 5 else "*" * len(word) for word in s.split()])

