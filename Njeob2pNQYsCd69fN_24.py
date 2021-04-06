
def prevent_distractions(txt):
  bad_words = ["anime", "vines", "meme", "roasts", "Danny DeVito"]
  if any(i in txt for i in bad_words):
    return "NO!"
  else:
    return "Safe watching!"

