
import re
​
def tweet(txt):
  txt_list = txt.split(" ")
  t = []
  for i in txt_list:
    if '@' in i or '#' in i:  
      i = re.sub(r'[^\w' + '@#' + ']', '', i)
      t.append(i)
  return " ".join(t)

