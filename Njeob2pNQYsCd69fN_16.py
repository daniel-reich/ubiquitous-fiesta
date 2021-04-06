
def prevent_distractions(txt):
  return 'NO!' if any(i in ["anime", "meme", "vines", "roasts", "DeVito"] for i in txt.split()) else 'Safe watching!'

