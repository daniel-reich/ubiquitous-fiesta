
def indexes(sentence, word):  
  indexes = []
  no_punct = ''
  for char in sentence:
    if char in '.",!':
      no_punct += ''
    else:
      no_punct += char.lower()
  word_list = no_punct.split(' ')
  for i in range(len(word_list)):
    if word_list[i] == word.lower():
      indexes.append(i)
  return indexes
    
​
​
def no_strangers(sentence):
  no_punct = ''
  for char in sentence:
    if char in '.",!':
      no_punct += ''
    else:
      no_punct += char.lower()
  word_list = no_punct.split(' ')
  acquaintance = []
  friend = []
  for word in word_list:
    if word_list.count(word) == 3 or word_list.count(word) == 4:
      if acquaintance.count(word) == 0:
        acquaintance.append(word)            
    elif word_list.count(word) >= 5:
      if friend.count(word) == 0:
        friend.append(word)
  return [sorted(acquaintance, key = lambda word: indexes(sentence, word)[2]), 
            sorted(friend, key = lambda word: indexes(sentence, word)[4])]

