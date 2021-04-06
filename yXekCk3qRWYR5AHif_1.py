
import re
​
def vow_replace(word, vowel):
  return re.sub('[aeiou]', vowel, word)

