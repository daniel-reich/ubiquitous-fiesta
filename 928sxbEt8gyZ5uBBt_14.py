
def wurst_is_better(txt):
  snags = ['kielbasa', 'chorizo', 'pepperoni', 'snorkers', 'gurka', 'merguez', 'naem', 'andouille', 'sausage', 'salami', 'moronga']
  txt = txt.split(' ')
  ans = []
  for x in txt:
    if x.lower() not in snags:
      ans.append(x)
    else:
      ans.append('Wurst')
  return ' '.join(ans)

