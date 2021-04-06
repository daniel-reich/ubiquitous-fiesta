
def waterjug(start, goal):
  q=[[0,0,start[2],0]] # queue
  tested=[[0,0,start[2]]]
  
  
  for x in range(0,1000): #limit tests
    if q==[]:
      return("No solution.")
    c=q.pop(0)   # get from queue: water in jugs
    counter=c.pop()+1
    if c==goal:
      print ("done",x,' ',counter-1)
      return counter-1
      
    for a in [0,1,2]: # test all combinations of refillment
      for b in [0,1,2]:
        neu=c[:]   # copy dataset
      
        move=min(start[b]-neu[b],neu[a]) #liquid to move
        if move>0 and a!=b:
          neu[a] -= move
          neu[b] += move
  
          if neu not in tested: # prevent loops
            tested.append(neu)
            neu.append(counter)
            q.append(neu)
            
  print(q)
  return("No solution.")

