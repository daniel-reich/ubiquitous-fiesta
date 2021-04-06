
import re
def retrieve(txt):
  txt = txt.strip('.')
  txt = txt.split()
  pattern = r'[aeiou]'
  res_lst = []
  for word in txt:
    if re.match(pattern, word, re.I):
      res_lst.append(word.lower())
  return res_lst

