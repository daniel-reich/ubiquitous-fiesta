
import re
​
def vow_replace(word, vowel):
  x = re.sub("e|a|i|o|u", vowel, word)
  return x

