
def truncate(txt, length):
  words = txt.split()
  roughcut = txt[:length]
  roughwords = roughcut.split()
  
  cleanwords = []
  
  for word in roughwords:
    if word in words:
      cleanwords.append(word)
  
  return ' '.join(cleanwords)

