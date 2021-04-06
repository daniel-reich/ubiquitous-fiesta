
def reverse_words(words):
  a = words.split(' ')
  b = a[::-1]
  c = ''
  for i in b:
    c += i
    c += " "
  return c[:-1]

