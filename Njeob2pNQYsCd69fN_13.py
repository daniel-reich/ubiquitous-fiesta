
def prevent_distractions(txt):
  return "NO!" if any(x in txt for x in ["anime", "meme", "vine", "roasts", "Danny DeVito"]) else "Safe watching!"

