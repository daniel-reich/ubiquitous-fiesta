
import re
def split(txt):
  vowelsRegex = re.compile(r'[aeiouAEIOU]')
  consonantsRegex = re.compile(r'[^aeiouAEIOU]')
  vowels = ''.join(vowelsRegex.findall(txt))
  consonants = ''.join(consonantsRegex.findall(txt))
  return vowels + consonants

