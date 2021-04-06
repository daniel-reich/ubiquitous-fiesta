
def wurst_is_better(txt):
  import re
  p = re.compile(r'Kielbasa|Chorizo|Moronga|Salami|Sausage|Andouille|Naem|Merguez|Gurka|Snorkers|Pepperoni', re.I)
  return p.sub('Wurst', txt)

