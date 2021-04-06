
def sentence_searcher(txt, n):
  def get_sentence_indexes(txt):
    
    indexes = []
    
    for n in range(len(txt)):
      item = txt[n]
      if '.' in item:
        indexes.append(n)
    
    return indexes
  def convert_neg_to_pos(txt, index):
    if index >= 0:
      return index
    else:
      return len(txt) - abs(index)
  
  gsi = get_sentence_indexes(txt.split())
  cntp = convert_neg_to_pos(txt.split(), n)
  #print(gsi, cntp)
  sentences = {n: txt.split('. ')[n-1] for n in range(1, 1 + len(txt.split('. ')))}
​
  n = 1
  
  for index in gsi:
    if cntp > index:
      n += 1
  
  return sentences[n] + '.' if '.' not in sentences[n] else sentences[n]

