
def currently_winning(scores):
  y =0
  o =0
  res =[]
  for i in range(0,len(scores),2):
    y+= scores[i]
    o+= scores[i+1]
    res.append('Y' if y>o else 'O' if y<o else 'T')
  return res

