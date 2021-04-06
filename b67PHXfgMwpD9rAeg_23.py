
import re
​
def plus_sign(txt):
  count = 0
  
  for x in txt:
    if x.isalpha():
      count += 1
      
  matches = re.findall('(?=\+\w\+)', txt)
  
  return len(matches) == count

