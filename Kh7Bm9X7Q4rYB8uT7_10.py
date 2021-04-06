
import re
​
def is_vowel_sandwich(s):
  if len(s) == 3:
    return bool(re.search(r"[^aeiou][aeiou][^aeiou]$", s, re.IGNORECASE))
  return False

