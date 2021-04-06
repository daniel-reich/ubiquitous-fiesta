
import string
def increasing_word_weights(s):
  s = s.translate(str.maketrans('', '', string.punctuation))
  a = list(map(lambda x: sum(map(lambda y: ord(y) ,x)), s.split()))
  return sorted(a) == a

