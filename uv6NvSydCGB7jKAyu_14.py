
def is_parsel_tongue(sentence):
  
  words = sentence.lower().split()
  
  for word in words:
    scount = word.count('s')
    sscount = word.count('ss')
    
    if scount != 0 and sscount == 0:
      return False
  return True

