
def x_pronounce(sentence):
  sentence2 = ''
  for i in range(0,len(sentence),1):
    if sentence[i]=='x' and sentence[i-1]==' ' and sentence[i+1]==' ':
      sentence2 += 'ecks'
    elif sentence[i]=='x' and sentence[i-1]==' ':
      sentence2 += 'z'
    elif sentence[i]=='x':
      sentence2 += 'cks'
    else:
      sentence2 += sentence[i]
  return sentence2

