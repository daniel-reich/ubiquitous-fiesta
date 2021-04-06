
def find_nemo(sentence):
  mystring = sentence.replace(",","")
  x = mystring.split(" ")
  print(x)
  if "Nemo" in x:
    val = x.index("Nemo") +1
    return "I found Nemo at " +str(val) +"!"
  else:
    return "I can't find Nemo :("

