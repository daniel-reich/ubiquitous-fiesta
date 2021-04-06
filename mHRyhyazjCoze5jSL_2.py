
import re
​
def double_swap(txt, c1, c2):
  text = txt.replace(c1, '-')
  text = text.replace(c2, c1)
  text = text.replace('-', c2)
  return text

