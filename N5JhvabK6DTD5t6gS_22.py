
def markdown(symb):
  return md(symb)
  
class md():
  def __init__(self,s):
    self.symbol = s
    
  def __call__(self,sentence,word):
    sentence = sentence.split()
    sentence = ' '.join([self.symbol+i+self.symbol if word.lower() in i.lower() else i for i in sentence])
    return sentence

