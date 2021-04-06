
import re
pattern = re.compile('|'.join(['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']), re.IGNORECASE)
def wurst_is_better(txt):
  return pattern.sub('Wurst', txt)

