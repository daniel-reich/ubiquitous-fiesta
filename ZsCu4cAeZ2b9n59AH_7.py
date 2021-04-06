
def lost_dog(*neighborhood):
  dogs = {}
  n_dog = 0
  for x, house in enumerate(neighborhood, start=1):
    for y, room in enumerate(house, start=1):
      if not room:
        n_dog += 1
        k = 'Dog{}'.format(n_dog)
        v = 'House ({}) and Room ({})'.format(x, y)
        dogs[k] = v
  return dogs or 'Dog not found!'

