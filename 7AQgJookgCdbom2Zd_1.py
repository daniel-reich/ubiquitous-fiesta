
import re
​
def pig_latin(txt):
  return re.sub(r"\b(\w)(\w*?)\b", r"\2\1ay", re.sub(r"\b([aeiou])", r"w\1", txt.lower())).capitalize()

