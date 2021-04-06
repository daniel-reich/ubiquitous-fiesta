
import string
def average_word_length(txt):
  s = txt.translate(str.maketrans('', '', string.punctuation))
  words = s.split()
  return round(sum(len(w) for w in words) / len(words), 2)

