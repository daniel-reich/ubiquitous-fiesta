
def dakiti(sentence):
  def get_indexs(sentence):
    dic = {}
    
    for word in sentence.split():
      k = None
      v = ''
      
      for l8r in word:
        try:
          k = int(l8r)
        except ValueError:
          v += l8r
      
      dic[k] = v
    
    return dic
  
  indexes = get_indexs(sentence)
  
  return ' '.join([indexes[index] for index in sorted(indexes.keys())])

