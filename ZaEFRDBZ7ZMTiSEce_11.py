
def find_nemo(sentence):
  return "I found Nemo at " + str(sentence.split().index("Nemo")+1) + "!" if "Nemo" in sentence.split() else "I can't find Nemo :("

