
import re
def average_word_length(txt):
  sum = 0
  txt = re.sub(r'[^\w\s]','',txt)
  words = txt.split() 
  for i in range (len(words)):
    sum += len(words[i])
  return round((sum/len(words)),2)

