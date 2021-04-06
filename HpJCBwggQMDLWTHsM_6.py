
import string
def average_word_length(txt):
  txt = txt.translate(str.maketrans({key: None for key in string.punctuation}))
  return round(sum([len(i) for i in txt.split(' ')])/len(txt.split(' ')),2)

