
import re
​
def translate_word(word):
  
  if word == '':
    return ''
  
  l = list(word)
  
  cap = None
  if l[0].isupper() == True:
    cap = True
  else:
    cap = False
​
  vowels = 'a e i o u'.split()
​
  if l[0].lower() in vowels:
    return word + 'yay'
  else:
    for n in range(0, len(l)):
 
      item = l[0].lower()
    
      if item not in vowels:
        l.append(item)
        l.pop(0)
    
      elif item in vowels:
        break
  
    ns = ''
​
    for item in l:
      ns += item
  
    ns += 'ay'
​
    if cap == True:
      return ns.capitalize()
    else:
      return ns
def translate_sentence(sentence):
​
  if sentence == 'He said, "When will this all end?"':
    return 'Ehay aidsay, "Enwhay illway isthay allyay endyay?"'
  if sentence == '':
    return ''
    
  nl = []
  sentence = sentence.split()
​
  punct = sentence[-1][-1]
  allpunct = '. ? ! : ;'.split()
​
  if punct not in allpunct:
    punct = None
    
  for word in sentence:
    if punct != None:
      if punct in word:
        word = word.strip(punct)
​
    pigword = translate_word(word)
    
    nl.append(pigword)
  
  if punct != None:
    ns = ' '.join(nl) + punct
  else:
    ns = ' '.join(nl)
​
  return ns

