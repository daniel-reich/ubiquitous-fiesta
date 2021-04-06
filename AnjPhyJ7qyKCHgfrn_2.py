
# Fix this incorrect code, so that all tests pass!
import re
def remove_vowels(string):
  result = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
  return result

