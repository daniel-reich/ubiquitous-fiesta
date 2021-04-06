
def is_parsel_tongue(sentence):
  l = sentence.split()
  for word in l:
    if 's' in word.lower():
      if 'ss' not in word.lower():
        return False
  
  return True

