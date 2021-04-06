
import re
​
def wurst_is_better(txt):
  regex = re.compile(r"Kielbasa|Chorizo|Moronga|Salami|Sausage|Andouille|Naem|Merguez|Snorkers|Pepperoni" , re.I)
  return re.sub(regex , "Wurst" , txt);

