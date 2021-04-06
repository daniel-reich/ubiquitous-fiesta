
def wurst_is_better(txt):
  change = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem',
    'merguez', 'gurka', 'snorkers', 'pepperoni', 'sausages']
  txt = list(txt.split(' '))
  wv = 0
  wurst = 'Wurst'
  returnstile = ''
  while wv <= len(txt) - 1:
    if txt[wv].lower() in change:
      txt.remove(txt[wv])
      txt.insert(wv, wurst)
    returnstile += txt[wv] + ' '
    wv += 1
  returnstile = returnstile.rstrip(' ')
  return returnstile

