
def can_find(bigrams, words):
  mydict = {}
  sentence = ''.join(words)
  for i in range (len(bigrams)):
    if bigrams[i] in sentence:
      mydict[bigrams[i]] = 1
    else:
      mydict[bigrams[i]] = 0
  for keys,values in mydict.items():
    if (values==0):
      return False
  return True

