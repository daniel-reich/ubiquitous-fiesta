
def maximum_score(tile_hand):
    lst = []
    for i in tile_hand:
        lst.append(i.get('score'))
    return sum(lst)

