
def flip(txt, spec):
  print(txt)
  if spec == "word":
    if ' ' not in txt:
      return txt[::-1]    
    return ' '.join([word[::-1] for word in txt.split(' ')])
  elif spec == "sentence":
    return ' '.join([word for word in txt.split(' ')[::-1]])

