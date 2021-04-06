
def wurst_is_better(txt):
  sausages = ['kielbasa', 'chorizo', 'moronga', 'salami', 
  'sausage', 'andouille', 'naem', 'merguez', 
  'gurka', 'snorkers', 'pepperoni']
  german = []
  for word in txt.split():
    if word.lower() in sausages:
      german.append('Wurst')
    else:
      german.append(word)
  return (' '.join(german))

