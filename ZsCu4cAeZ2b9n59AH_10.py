
def lost_dog(*houses):
    dogs = {}
    c = 1
​
    for i, h in enumerate(houses, start=1):
        if 0 in h:
            dogs['Dog{}'.format(c)] = 'House ({}) and Room ({})'.format(i, h.index(0) + 1)
            c += 1
​
    return dogs or 'Dog not found!'

