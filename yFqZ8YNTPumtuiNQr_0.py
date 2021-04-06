
import re
​
def eadibitan(word):
  C, V = '[^aeiou]', '[aeiouy]'
  syllable = '({}?)({}?)({})({}?{}?)({}?(?!{}))'.format(C,C,V,V,V,C,V)
  return re.sub(syllable, r'\2\3\1\4\5', word)

