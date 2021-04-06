
def wurst_is_better(txt):
  sausages = {'Kielbasa', 'Chorizo', 'Moronga', 'Salami', 'Sausage',
  'Andouille', 'Naem', 'Merguez', 'Gurka', 'Snorkers', 'Pepperoni'}
  res = []
  for word in txt.split():
    singularized_word = word[:-1]
    if word.capitalize() in sausages:
      res.append('Wurst')
    elif singularized_word.capitalize() in sausages:
      res.append('Wursts')
    else:
      res.append(word)
  return ' '.join(res)

