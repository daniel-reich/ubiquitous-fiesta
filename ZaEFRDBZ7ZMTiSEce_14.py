
def find_nemo(sentence):
  temp = sentence.split(' ')
  if 'Nemo' in temp:
    return "I found Nemo at "+str(temp.index('Nemo')+1)+"!"
​
  return "I can't find Nemo :("

