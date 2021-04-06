
def get_path_length(world, width, height):
  w=world.split(',')
  w.extend('ttt'*width)
  print(w)
  m=w.index('m') #start
  h=w.index('h') #end
  q=[m] # queue
  r={m:0}
  
  while q: 
    p=q.pop(0)
    #print("pop:", p)
    if w[p]=='h':
      print("####")
      return r[p]
    for i in [-1,0,1]:
      for ii in [-1,0,1]:
        for c in [1]:#range(1,max(width,height)): # for not steps but changes in directions
          neu=p+(i+ii*(width))*c
          if neu>=0 and neu!=p and w[neu]!='t' and neu not in r and (p) // (width) == (p+i*c) // (width) :
            q.append(neu)
            r[neu]=r[p]+1
            #print(neu, r[neu])
            if neu==h:
              return r[p]+1
          else:
            break
    #print(q)
  return(-1)

