
from re import findall
​
def average_word_length(txt):
  txt = list(map(len, findall(r'\w+', txt)))
  return round(sum(txt) / len(txt), 2)

