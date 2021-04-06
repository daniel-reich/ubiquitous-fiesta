
def find_nemo(sentence):
  nemo = sentence.split()
  if "Nemo" in nemo:
    return "I found Nemo at "+str(nemo.index('Nemo')+1) +'!'
  else:
    return "I can't find Nemo :("

