
def find_nemo(sentence):
  return "I can't find Nemo :(" if 'Nemo' not in sentence.split(' ') else "I found Nemo at {}!".format(sentence.split(' ').index('Nemo')+1)

