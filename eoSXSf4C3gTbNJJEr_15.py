
def find_cadence(chords):
  y=[]
  for x in chords:
    y.append(x.lower())
  print(y)
​
  if y[-1] == "v":
    return('imperfect') 
  elif y[-2] == "v" and y[-1] == "i":
    return('perfect')
  elif y[-2] == "iv" and y[-1] == "i":
    return('plagal')
  elif y[-2] == "v" and y[-1]!= "i":
    return('interrupted')
  else:
    return('no cadence')

