
def reverse_words(words):
  a = words.strip()
  b = a.split(' ')
  return ' '.join(b[::-1])

