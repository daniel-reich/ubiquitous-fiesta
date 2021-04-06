
def sum_of_vowels(sentence):
  di={'A':4,'E':3,'I':1,'O':0,'U':0}
  sum=0
  for s in sentence:
    if s.upper() in di:
      sum+=di[s.upper()]
  return sum

