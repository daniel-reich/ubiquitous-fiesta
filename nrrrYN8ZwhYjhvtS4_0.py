
import re
​
def extend_vowels(word, num):
  return re.sub(
    '[aeiouAEIOU]', 
    lambda x: (num + 1) * x.group(), 
    word
  ) if not num % 1 and num >= 0 else 'invalid'

