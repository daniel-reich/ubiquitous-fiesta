
def lost_dog(*houses):  
    d = {}
    dog = 1
    for h, house in enumerate(houses, start=1):
        if 0 in house:
            k = 'Dog' + str(dog)
            dog += 1
            r = house.index(0) + 1
            v = 'House (' + str(h) + ') and Room (' + str(r) + ')'
            d[k] = v
    if d:
        return d
    else:
        return 'Dog not found!'

