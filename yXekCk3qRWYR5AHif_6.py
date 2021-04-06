
import re
def vow_replace(word, vowel):
  word = re.sub('[aeiou]', vowel, word)
  return word

