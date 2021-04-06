
import re
def longest_7segment_word(l):
  x = lambda i: re.findall('[kmvwx]',i)
  if all(len(x(i))>0 for i in l): return ''
  return max([i for i in l if not x(i)], key=len)

