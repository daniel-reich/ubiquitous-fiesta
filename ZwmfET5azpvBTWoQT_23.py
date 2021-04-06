
def valid_word_nest(word, nest):
  l = -1
  i = len(nest)//len(word)
  nest_lenght = len(nest) 
  b = []
  while i>0:
    nest = ''.join(nest.split(word))
    b.append(nest_lenght - len(word)*(l+2)== len(nest))
    l+=1
    i-=1
  return True if not nest and all(b) else False

