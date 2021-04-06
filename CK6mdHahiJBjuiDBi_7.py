
weights = [2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2]
bags = 4
def can_fit(weights, bags):
    maxw = 10*bags
    for i in weights:
        maxw-=i
    if maxw>=0:
        return True 
    else:
        return False
can_fit(weights, bags)

