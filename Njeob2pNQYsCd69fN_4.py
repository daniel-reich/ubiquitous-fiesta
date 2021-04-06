
def prevent_distractions(txt):
  verboten = ["anime","meme","vines","roasts","Danny DeVito"]
  for key in verboten:
    if key in txt:
      return("NO!")
  return("Safe watching!")

