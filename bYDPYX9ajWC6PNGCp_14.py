
def track_robot(*lst):
  movement = {0:"+y",1:"+x",2:"-y",3:"-x"}
  robot = [0,0]
  counter = 0
  for i in lst:
      if(movement[counter] == "+x"):
          robot[0]+=i
      elif(movement[counter] == "+y"):
          robot[1]+=i
      elif(movement[counter] == "-x"):
          robot[0]-=i
      elif(movement[counter] == "-y"):
          robot[1]-=i
      counter+=1
      if(counter>3):
          counter=0
  return robot

