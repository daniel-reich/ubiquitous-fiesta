
def average_word_length(txt):
  words = [word.strip(',.?!') for word in txt.split()]
  return round(sum(len(word) for word in words) / len(words), 2)

