
import re
​
def split(txt):
  vowels = ''.join(char for char in txt if char in 'aeiou')
  return vowels + re.sub('[aeiou]', '', txt)

