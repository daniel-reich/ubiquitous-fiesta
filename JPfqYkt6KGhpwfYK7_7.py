
import re
​
def replace_the(txt):
  txt = re.sub(r"\bthe (?=[aeiou])", r"an ", txt)
  txt = re.sub(r"\bthe\b", r"a", txt)
  
  return txt

