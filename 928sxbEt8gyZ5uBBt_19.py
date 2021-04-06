
sausages = [
    'Kielbasa', 'Chorizo', 'Moronga', 'Salami', 'Sausage',
  'Andouille','Naem','Merguez','Gurka','Snorkers','Pepperoni'
]
def wurst_is_better(txt):
  for s in sausages:
    txt = txt.replace(s, 'Wurst')
    txt = txt.replace(s.lower(), 'Wurst')
  return txt

