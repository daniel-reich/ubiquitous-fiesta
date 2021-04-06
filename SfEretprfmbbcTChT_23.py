
def reverse_words(words):
  return ' '.join(list(filter(None, words.split()))[::-1])

