
def lost_dog(*alist):
    newlist = {}
    prefix = 'Dog'
    dog_count = 1
    for i in range(len(alist)):
        house = alist[i]
        for j in range(len(house)):
            if house[j] == 0:
                newlist['Dog{}'.format(dog_count)] = 'House ({}) and Room ({})'.format(i+1,j+1)
                dog_count += 1
                break
    if len(newlist) == 0:
        return 'Dog not found!'
    else:
        return newlist

