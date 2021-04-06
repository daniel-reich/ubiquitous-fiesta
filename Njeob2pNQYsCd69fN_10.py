
def prevent_distractions(txt):
  banned = ["anime", "meme", "vine", "roasts", "Danny Devito"]
  for i in banned:
    if txt.find(i) != -1: return "NO!"
  return "Safe watching!"

