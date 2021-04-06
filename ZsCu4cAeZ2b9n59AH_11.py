
def lost_dog(*args):
  ret = {}
  d = 1
  for i in range(len(args)):
    for j in range(len(args[i])):
      if args[i][j]==0:
        ret['Dog'+str(d)] = 'House ('+str(i+1)+') and Room ('+str(j+1)+')'
        d+=1
  return ret if ret else 'Dog not found!'

