
def alternating_caps(txt):
  
  words = txt.split()
  cap = True
  new_words =[]
  
  for word in words:
    newword = ''
    for l8r in word:
      if cap == True:
        newword += l8r.upper()
        cap = False
      elif cap == False:
        newword += l8r.lower()
        cap = True
    new_words.append(newword)
  
  return ' '.join(new_words)

