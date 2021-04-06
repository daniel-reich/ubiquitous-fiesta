
def reverse_words(words):
  t=words.split()
  i=1
  return ' '.join([t[-(i+1)] for i in range(len(t))])

