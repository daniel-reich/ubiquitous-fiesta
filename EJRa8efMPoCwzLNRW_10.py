
def dakiti(sentence):
  ind = [int(i)-1 for i in sentence if i.isnumeric()]
  words = [i for i in sentence.split()]
  output = []
  for i in range(len(ind)):
    output.append(' ')
  for i,j in enumerate(ind):
    output[j]=''.join([k for k in words[i] if k not in '0123456789'])
  return ' '.join(output)
  
  #I dont understand how using words[i] resulted in the right answer, but I'll take it

