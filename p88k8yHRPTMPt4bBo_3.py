
import re
​
def countVowels(str):
  return len(re.findall(r'[aeiou]', str))

