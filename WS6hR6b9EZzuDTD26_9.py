
def no_duplicate_letters(phrase):
  return all(len(word) == len(set(word)) for word in phrase.split())

