
def w_replace(word):
  new_word = word.replace('.','') \
    .replace(',','') \
    .replace("'",'')\
    .replace('!','')
    
  if new_word.endswith('nts'):
    return new_word.replace('nts','nce') + word[word.index('nts')+3:]
  elif new_word.endswith('nce'):
    return new_word.replace('nce', 'nts') + word[word.index('nce')+3:]
  else:
    return word
​
def switcheroo(txt):
  return ' '.join(map(w_replace, [w for w in txt.split()]))

