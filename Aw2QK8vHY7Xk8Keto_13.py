
def longest_word(s):
  word = s.split(' ')
  f = ''
  for w in word:
    if len(w) > len(f):
      f = w
  return f

