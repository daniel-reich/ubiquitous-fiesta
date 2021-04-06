
import re
​
def average_word_length(txt):
  txt = (re.sub(r'[^\w\s]','',txt)).split()
  return round(sum(len(word) for word in txt)/len(txt),2)

