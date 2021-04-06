
def average_word_length(txt):
  lengths = [len(word.rstrip(',.!?')) for word in txt.split()]
  return round(sum(lengths) / len(lengths), 2)

