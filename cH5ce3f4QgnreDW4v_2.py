
def maximum_score(tile_hand):
    answer = 0
    
    for i in tile_hand:
        answer += i['score']
    return answer

