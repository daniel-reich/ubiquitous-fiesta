
import re
def remove_vowels(txt):
  return re.sub(r'[AEIOU]', '', txt, flags=re.IGNORECASE)

