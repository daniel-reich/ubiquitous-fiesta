
def map_letters(word):
  d={}
  for i in range(len(word)):
    if word[i] in d:
      d[word[i]].append(i)
    else: 
      d[word[i]] = [i]
  
  return d

