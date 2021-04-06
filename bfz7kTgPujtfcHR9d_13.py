
def x_pronounce(sentence):
  new_sentence = ""
  list_sentence = sentence.split(" ")
  for word in list_sentence:
    if word == "x":
      new_sentence += "ecks"
    elif word[0] == "x":
      new_sentence += "z" + word[1:]
    else:
      new_sentence += word #+ " "
    new_sentence = new_sentence.replace("x", "cks") + " "
    #new_sentence.pop([-1])
  return new_sentence[0:-1]

