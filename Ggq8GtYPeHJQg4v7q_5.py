
import re
​
def replace_vowels(txt, ch):
  return re.sub('[aeouiAEOUI]', ch, txt)

