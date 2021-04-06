
import re
​
def wurst_is_better(s):
  sausages = ['Kielbasa', 'Chorizo', 'Moronga', 'Salami', 'Sausage',
    'Andouille', 'Naem', 'Merguez', 'Gurka', 'Snorkers', 'Pepperoni']
  return re.sub(r'|'.join(sausages), 'Wurst', s, flags=re.IGNORECASE)

