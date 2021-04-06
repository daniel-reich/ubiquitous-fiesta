
def average_word_length(txt):
  sum_alpha = sum(i.isalpha() for i in txt)
  avg_word = round(sum_alpha / len(txt.split()), 2)
  return avg_word

