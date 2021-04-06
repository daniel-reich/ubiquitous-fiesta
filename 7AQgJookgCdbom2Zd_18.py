
def pig_latin(txt):
  end = txt[-1]
  txt = txt[:-1]
  revise =  ' '.join([(word + "way").lower() if word[0] in "aeiouAEIOU" else (word[1:] + word[0] + "ay").lower() for word in txt.split()])  
  revise += end
  return revise.capitalize()

