
import string as s
​
def average_word_length(txt):
  cln = txt.translate(str.maketrans('', '', s.punctuation)).split()
  return round(sum(len(x) for x in cln)/len(cln),2)

