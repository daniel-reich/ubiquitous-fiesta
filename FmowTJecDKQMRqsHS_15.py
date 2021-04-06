
def crop_hydrated(field):
  dict={}
  i=0
  while i<len(field):
    j=0
    while j<len(field[0]):
      if field[i][j]=="w":
        dict[(i-1,j-1)]=True
        dict[(i-1,j)]=True
        dict[(i-1,j+1)]=True
        dict[(i,j-1)]=True
        dict[(i,j+1)]=True
        dict[(i+1,j-1)]=True
        dict[(i+1,j)]=True
        dict[(i+1,j+1)]=True
      j+=1
    i+=1
  i=0
  while i<len(field):
    j=0
    while j<len(field[0]):
      if field[i][j]=="c":
        if not dict.get((i,j),False):
          return False
      j+=1
    i+=1
  return True

