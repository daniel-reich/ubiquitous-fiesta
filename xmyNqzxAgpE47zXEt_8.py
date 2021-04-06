
import re
​
def is_alphabetically_sorted(sentence):
  return any(i==''.join(sorted(i)) and len(i)>=3 for i in re.split('[\s\.]', sentence))

