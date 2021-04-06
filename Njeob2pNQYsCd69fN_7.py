
def prevent_distractions(txt):
  words = ("anime", "meme", "vines", "roasts", "Danny Devito")
  for word in words:
    if word in txt:
      return "NO!"
  return "Safe watching!"

