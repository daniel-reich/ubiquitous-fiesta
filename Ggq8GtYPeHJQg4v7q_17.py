
import re
​
def replace_vowels(txt, ch):
  return ch.join(re.split('[aeiouAEIOU]', txt))

