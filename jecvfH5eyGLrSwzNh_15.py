
def fauna_number (txt):
  other_words  = ['There','are','and']
  animals_list = []
  number_list  = []
  animals      = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
  word_str     = ''
  word         = []
  ans          = []
  valid_index  = []
  
  for i in txt:
    while i!= '.' and i!=' ' and i!= ',':
      word.append (i)
​
      break
    
    if i == '.' or i == ',' or i == ' ':
      for b in word:
        word_str+= b
​
      try:
          int (word_str)
          number_list.append (word_str)
​
      except:
          if word_str not in other_words:
            animals_list.append (word_str)
​
      word  = []
      word_str = ''
​
   
  for i in range (len (animals_list)):
    if animals_list[i] in animals:
      valid_index.append (i) 
  for c in valid_index:
    tup = (animals_list[c],number_list[c])
​
    ans.append (tup) 
  return ans

