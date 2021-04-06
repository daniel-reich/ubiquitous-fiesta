
def find_shortest_words(txt):
  words = [word.rstrip('.,?!').lower() for word in txt.split() if word.rstrip('.,!?').isalpha()]
  minimum = min([len(word) for word in words])
  return sorted([word for word in words if len(word) == minimum])

