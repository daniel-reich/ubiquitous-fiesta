
import re
​
def average_word_length(txt):
  txt = re.sub(r'[^\w\s]','', txt)
  
  return round(sum(len(i) for i in txt.split(' ')) / len(txt.split(' ')),2)

