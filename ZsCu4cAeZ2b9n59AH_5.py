
def lost_dog(*houses):
  dogs = {}
  for i,e in enumerate(houses):
    if 0 in e:
      dogs['Dog{}'.format(len(dogs)+1)] = 'House ({}) and Room ({})'.format(i+1,e.index(0)+1)
  return dogs if len(dogs)>0 else 'Dog not found!'

