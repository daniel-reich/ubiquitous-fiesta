
def find_nemo(sentence):
  try:
    return "I found Nemo at %d!" %(sentence.split(' ').index("Nemo")+1)
  except:
    return "I can't find Nemo :("

