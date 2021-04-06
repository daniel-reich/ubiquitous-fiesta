
def increasing_word_weights(sentence):
  def weight_finder(word):
    l = list(word)
    exclude = '/ ! , . ? \" \' @ : ; # ~'.split() #It is important to remove any punctuation as this throws off the calcuations!
    
    codes = []
    
    for l8r in l:
      if l8r not in exclude:
        code = ord(l8r)
        codes.append(code)
    
    s = sum(codes)
    
    return s
  
  word_weights = {}
  values = []
  
  sentence = sentence.split()
  
  for word in sentence:
    
    value = weight_finder(word)
    
    if value not in word_weights:
      word_weights[value] = [word]
    else:
      word_weights[value].append(word)
    
    if value not in values:
      values.append(value)
  
  values = sorted(values)
  
  sorted_words = []
  
  for value in values:
    words = word_weights[value]
    for word in words:
      sorted_words.append(word)
  
  if sorted_words == sentence:
    return True
  else:
    return False

