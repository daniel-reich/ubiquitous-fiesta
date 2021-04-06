
def no_duplicate_letters(phrase):
  words = phrase.split()
  return all(len(set(word)) == len(word) for word in words)

