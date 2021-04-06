
def find_nemo(sentence):
  if "Nemo" in sentence.split():
    d = sentence.split()
    e = 0
    for word in d:
      e +=1
      if word == "Nemo":
        return "I found Nemo at "+ str(e) +"!"
    
  else:
    return "I can't find Nemo :("

