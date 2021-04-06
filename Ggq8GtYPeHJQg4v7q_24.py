
import re
​
def replace_vowels(txt, ch):
  return re.sub('[aieou]', ch, txt)

