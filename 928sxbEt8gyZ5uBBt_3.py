
def wurst_is_better(txt):
  sausages = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']
  for i in sausages:
    txt = txt.replace(i,"Wurst")
    txt = txt.replace(i.capitalize(),"Wurst")
  return txt

