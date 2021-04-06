
def find_shortest_words(txt):
  words = txt.lower().split()
  words = [word.strip(".,?!%:") for word in words if word.strip(".,?!%:").isalpha()]
  return sorted([word for word in words if len(word) == len(min(words, key=len))])

