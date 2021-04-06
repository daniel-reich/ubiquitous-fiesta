
def find_nemo(sentence):
  idx = [i for i,j in enumerate(sentence.split()) if j=='Nemo']
  if not idx: return "I can't find Nemo :("
  return 'I found Nemo at {}!'.format(idx[0]+1)

