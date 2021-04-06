
def average_word_length(txt):
  return round(sum(i.isalpha() for i in txt)/(txt.count(" ") + 1), 2)

