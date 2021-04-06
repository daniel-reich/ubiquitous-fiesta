
def camelCasing(txt):
  txt = txt.replace('_', ' ')
  txt = txt.split()
  
  words = []
  first = False
​
  for item in txt:    
    if first == False:
      word = item.lower()
      words.append(word)
      first = True
      continue
    elif first == True:
      word = item.capitalize()
      words.append(word)
  
  return ''.join(words)

