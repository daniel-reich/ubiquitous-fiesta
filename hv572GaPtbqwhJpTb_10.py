
def elasticize(word):
  return ''.join(v*min(i+1,len(word)-i) for i,v in enumerate(word))

