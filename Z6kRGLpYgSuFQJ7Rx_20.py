
import re
def find_longest(sentence):
  A=re.findall('(?i)\w+', sentence)
  return max(A, key=len).lower()

