
def climb(stamina, obstacles):
  v=0
  for s in range(len(obstacles)):
    if s==len(obstacles)-1:
      return v
    if obstacles[s]<obstacles[s+1]:
      e=obstacles[s+1]-obstacles[s]
      e=int(e)+1
      stamina-=2*e
      if stamina<0:
        return v
      else:
        v+=1
      e=0
    elif obstacles[s]>obstacles[s+1]:
      e=obstacles[s]-obstacles[s+1]
      e=int(e)+1
      stamina-=e
      if stamina<0:
        return v
      else:
        v+=1
      e=0
    else:
      v+=1
  return v

