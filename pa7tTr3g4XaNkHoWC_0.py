
def pig_latin_sentence(sentence):
  def pig(w):
    r = min(i for i in range(len(w)) if w[i] in "aeiou")
    return w[r:] + w[:r] + "w"*(r==0) +"ay"
  
  return " ".join(pig(w) for w in sentence.split(" "))

