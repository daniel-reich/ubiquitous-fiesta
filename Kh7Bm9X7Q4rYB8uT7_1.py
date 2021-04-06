
import re
​
def is_vowel_sandwich(s):
  return bool(re.match(r'[^aeiou][aeiou][^aeiou]\Z', s))

