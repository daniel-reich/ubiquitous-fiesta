
def pig_latin_sentence(sentence):
  res=[]
  for w in sentence.split():
    if w[0] in 'aeiou':res+=[w+'way']
    else:
      while not w[0] in 'aeiou':
        w=w[1:]+w[0]
      res+=[w+'ay']
  return ' '.join(res)

