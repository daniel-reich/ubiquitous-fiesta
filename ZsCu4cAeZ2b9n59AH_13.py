
def lost_dog(*houses):
  dogs = {}
  for i in range(len(houses)):
    for j in range(len(houses[i])):
      if houses[i][j] == 0:
        dogs['Dog'+str(len(dogs)+1)] = "House (" + str(i+1) + ") and Room (" + str(j+1) + ")"
  if dogs == {}:
    return "Dog not found!"
  return dogs

