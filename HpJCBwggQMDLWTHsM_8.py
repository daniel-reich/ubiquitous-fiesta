
import re
def average_word_length(txt):
  s = re.sub(r'[^\w\s]','',txt)
  return round(sum([len(i) for i in s.split()]) / len(s.split()), 2)

