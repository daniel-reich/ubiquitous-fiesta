
def wurst_is_better(txt):
  sausages = ['kielbasa','chorizo','moronga','salami','sausage','andouille','naem','merguez','gurka','snorkers','pepperoni']
  result = txt.split()
  for i in range(len(result)):
    if result[i].lower() in sausages:
      result[i] = 'Wurst'
  return ' '.join(result)

