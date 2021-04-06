
def find_nemo(sentence):
  for e,i in enumerate(sentence.split(' ')):
    if i == "Nemo":
      return "I found Nemo at {}!".format(str(e+1))
    else:
      pass
  return "I can't find Nemo :("

