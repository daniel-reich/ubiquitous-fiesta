
def lost_dog(*lst):
  dogs, res = 0, {}
  
  for i in range(len(lst)):
    if 0 in lst[i]:
      dogs += 1
      k = 'Dog{}'.format(dogs)
      v = 'House ({}) and Room ({})'.format(i + 1, lst[i].index(0) + 1)
      res.update({k: v})
​
  return res if dogs else 'Dog not found!'

