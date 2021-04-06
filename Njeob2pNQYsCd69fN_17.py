
def prevent_distractions(txt):
  u = 0
  x = txt.split(" ")
  y = ["anime","meme","vine","roasts","Danny","vines"]
  for i in x:
    for n in y:
      if i.lower() == n.lower():
        u += 1
  if int(u) > 0:
    return 'NO!'
  if int(u) == 0:
    return "Safe watching!"

