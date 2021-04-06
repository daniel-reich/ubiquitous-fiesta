
import re
def vowel_links(txt):
  return bool(re.findall('[aeiou] [aeiou]', txt))

