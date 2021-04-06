
def freed_prisoners(prison):
  block=prison
  free=0
  if block[0]==0:
    free=0
  else:
    for i in range(0,len(block)):
        if block[i]==True:
            free+=1
            for i in range(0,len(block)):
                if block[i]==True:
                    block.pop(i)
                    block.insert(i,False)
                else:
                    block.pop(i)
                    block.insert(i,True)
  return free

