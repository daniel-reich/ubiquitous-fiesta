
def prevent_distractions(txt):
  l=["anime", "meme", "vine", "roasts", "Danny DeVito"]
​
      
  if any(i in txt for i in l):
    return "NO!"
  else:
    return "Safe watching!"

