
import re
def double_swap(txt, c1, c2):
  word=""
  for i in txt:
    if i==c1:
      word+=c2
    elif i==c2:
      word+=c1
    else:
      word+=i
  return word

