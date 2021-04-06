
def find_nemo(sentence):
  for i in sentence.split(" "):
    if i=="Nemo": return "I found Nemo at "+str(sentence.split(" ").index("Nemo")+1)+"!"
  else: return "I can't find Nemo :("

