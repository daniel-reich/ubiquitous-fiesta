
import re
​
def wurst_is_better(txt):
  all = re.findall(r"Kielbasa|Chorizo|Moronga|Salami|Sausage|Andouille|Naem|Merguez|Gurka|Snorkers|Pepperoni", txt, re.I)
  for item in all:
    txt = txt.replace(item, "Wurst")
  return txt

