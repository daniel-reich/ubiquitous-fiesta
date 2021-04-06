
import string
def average_word_length(txt):
  arr = [i.strip(string.punctuation) for i in txt.split()]
  return round(sum([len(i.strip(string.punctuation)) for i in txt.split()])/len(arr),2)

