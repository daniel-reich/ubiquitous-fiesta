
def letters(word1, word2):
  set_1,set_2=set(word1),set(word2)
  
  common_words=list(''.join(str(x) for x in set_1.intersection(set_2)))
  unique1=list(''.join(str(x) for x in set_1-set_2))
  unique2=list(''.join(str(x) for x in set_2-set_1))
  common_words.sort()
  unique1.sort()
  unique2.sort()
  
  common_words=''.join(str(x) for x in common_words)
  unique1=''.join(str(x) for x in unique1)
  unique2=''.join(str(x) for x in unique2)
  
  return [common_words,unique1,unique2]

