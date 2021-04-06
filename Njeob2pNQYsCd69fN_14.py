
def prevent_distractions(txt):
  words=["anime","meme","vine","roasts","danny devito"]
  answer='Safe watching!'
  for i in words:
    if i in txt.lower():
      return 'NO!'
  
  return answer

