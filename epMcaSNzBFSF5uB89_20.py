
def currently_winning(scores):
  winning=[]
  yTotal=0
  oTotal=0
  yscores=scores[::2]
  oscores=scores[1::2]
  for x in range(len(yscores)):
    yTotal=yscores[x]+yTotal
    oTotal=oscores[x]+oTotal
    if yTotal>oTotal:
      winning.append('Y')
    if oTotal>yTotal:
      winning.append('O')
    if yTotal==oTotal:
      winning.append('T')
  return winning

