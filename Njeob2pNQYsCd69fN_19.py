
def prevent_distractions(txt):
  a = ["anime",
"meme",
"vine",
"roasts",
"Danny Devito"]
  for i in a:
    if i in txt:
      return "NO!"
  return "Safe watching!"

