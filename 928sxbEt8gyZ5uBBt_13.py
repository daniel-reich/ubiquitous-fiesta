
def wurst_is_better(txt):
  sausages = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']
  
  for item in sausages:
    if item in txt: txt = txt.replace(item, 'Wurst')
    if item.capitalize() in txt: txt = txt.replace(item.capitalize(), 'Wurst')
​
  return txt

