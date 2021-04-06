
import re
​
def find_longest(sentence):
  return max(re.split('[^A-Za-z]', sentence), key=len).lower()

