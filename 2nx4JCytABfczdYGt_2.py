
def conjugate(verb, pronoun):
  
  Text = str(verb)
  
  Cursor = -1
  
  while (Cursor >= -3):
    Text = Text[0:-1]
    Cursor -= 1
  
  if (Text[-1] == "c") or (Text[-1] == "g"):
    Text = Text + "h"
  
  if (pronoun == 1):
    Sentence = "Io " + Text + "o"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  elif (pronoun == 2):
    Sentence = "Tu " + Text + "i"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  elif (pronoun == 3):
    Sentence = "Egli " + Text + "a"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  elif (pronoun == 4):
    Sentence = "Noi " + Text + "iamo"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  elif (pronoun == 5):
    Sentence = "Voi " + Text + "ate"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  elif (pronoun == 6):
    Sentence = "Essi " + Text + "ano"
    Sentence = Sentence.replace("ii","i")
    return Sentence
  
  else:
    return "I Don't Know!"

