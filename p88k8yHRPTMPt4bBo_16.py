
import re
def count_vowels(txt):
  y = 0;
  y += len(re.findall("a",txt))
  y += len(re.findall("e",txt))
  y += len(re.findall("i",txt))
  y += len(re.findall("o",txt))
  y += len(re.findall("u",txt))
  return y

