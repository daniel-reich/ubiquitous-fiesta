
def prevent_distractions(txt):
  banned = ["anime", "meme", "vine", "roasts", "Danny DeVito"]
  for i in banned:
    if txt.find(i) != -1:
      return "NO!"
      
  return "Safe watching!"

