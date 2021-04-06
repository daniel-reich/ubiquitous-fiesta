
import re
def count_vowels(txt):
  return len(re.findall(r'([aeiou]{1})', txt))

