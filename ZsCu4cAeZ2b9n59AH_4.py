
def lost_dog(*houses):
  
  dog = lambda house: house.index(0) if 0 in house else None
  houses = {n+1: dog(houses[n]) for n in range(len(houses))}
  c = 1
  dogs = {}
  
  for n in houses.keys():
    print(n)
    house = houses[n]
    print(house)
    if house != None:
      dogs['Dog{}'.format(c)] = 'House ({}) and Room ({})'.format(n, house + 1)
      c += 1
      
  return dogs if 'Dog1' in dogs.keys() else 'Dog not found!'

