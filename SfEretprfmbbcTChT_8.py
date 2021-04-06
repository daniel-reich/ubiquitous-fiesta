
def reverse_words(words):
  return ' '.join([w for w in words.split() if w][::-1])

