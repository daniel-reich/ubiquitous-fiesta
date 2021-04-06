
import re
def first_n_vowels(txt, n):
  vowels = ''.join(re.findall('[aeiou]',txt))
  if n > len(vowels):
    return 'invalid'
  return vowels[:n]

