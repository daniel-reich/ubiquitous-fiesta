
def final_direction(i, t):
    direction = {0: 'N', 1: 'E',  2: 'S', 3: 'W'}
    return direction[((sum([-1 if l == 'L' else 1 for l in t]))+list(direction.keys())[list(direction.values()).index(i)])%4]

