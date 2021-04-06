
def maximum_score(tile_hand):
    sum=0
    for i in tile_hand:
        x=i.get("score")
        sum=sum+x
    return sum

