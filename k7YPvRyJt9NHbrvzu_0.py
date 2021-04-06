
def football(score):
    ways = [1] + [0]*score
    for val in (2, 3, 6, 7, 8):
        for i in range(val, score + 1):
            ways[i] += ways[i-val]
    return ways[score]

