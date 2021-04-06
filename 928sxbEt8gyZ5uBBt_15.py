
def wurst_is_better(txt):
  wursts = ['kielbasa','chorizo','moronga','salami','sausage','andouille','naem','merguez','gurka','snorkers','pepperoni']
  lst = []
  l1 = txt.split()
  for word in l1:
    if word.lower() in wursts:
      lst.append('Wurst')
    else:
      lst.append(word)
  return ' '.join(lst)

