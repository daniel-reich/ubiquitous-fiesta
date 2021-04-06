
def available_spots(lst, num):
  parity = num%2  #looking to have 1 neighbour share the parity
  likedSpots = 0
  for x in range(len(lst)-1):
    if(lst[x]%2 == parity or lst[x+1]%2 == parity):
      likedSpots += 1
      
  return likedSpots

