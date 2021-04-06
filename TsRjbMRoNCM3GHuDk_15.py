
import re
​
def syllabification(word):
  return re.sub(r'(.[aAeiou])', r'.\1', word)[1:]

