
def find_nemo(sentence):
  array=sentence.split(" ")
  for i in range(len(array)):
    if array[i]=="Nemo":
      return "I found Nemo at "+str(i+1)+"!"
  return "I can't find Nemo :("

