
def prevent_distractions(txt):
  lst = [
    'anime',
    'meme',
    'vine',
    'roasts',
    'Danny DeVito'
  ]
  
  for i in lst:
    if i in txt:
      return "NO!"
      
  return "Safe watching!"

