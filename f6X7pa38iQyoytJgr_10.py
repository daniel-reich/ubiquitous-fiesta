
def increasing_word_weights(s):
  l = [sum(ord(l) for l in w if l.isalpha()) for w in s.split()]
  return l == sorted(l)

