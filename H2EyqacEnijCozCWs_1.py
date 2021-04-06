
import re
​
def first_n_vowels(txt, n):
  found = re.findall(r'[aeiou]', txt)
  return ''.join(found)[:n] if len(found) >= n else 'invalid'

