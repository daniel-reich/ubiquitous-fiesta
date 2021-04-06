
import re
def vowel_links(txt):
  x = re.findall(r'[aeiou]\s[aeiou]', txt)
  if len(x) == 0:
    return False
  else:
    return True

