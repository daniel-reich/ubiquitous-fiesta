
def find_nemo(sentence):
  array=sentence.split(' ')
  for i in array:
    if i=='Nemo':
      return "I found Nemo at "+str(array.index(i)+1)+"!"
  return "I can't find Nemo :("

