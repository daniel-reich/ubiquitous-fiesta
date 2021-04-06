
import copy
​
def evolve_brick(brick):
    new_brick = copy.deepcopy(brick)
    # pad edges of brick:
    brick = [[25] * 12] + brick + [[25] * 12]
    for i in range(1, 11):
        brick[i] = [25] + brick[i] + [25]
    for r in range(1, 10):
        for c in range(1, 11):
            T_sum = 0
            for r2 in range(r - 1, r + 2):
                for c2 in range(c - 1, c + 2):
                    T_sum += brick[r2][c2]
            new_brick[r-1][c-1] = int(round(T_sum / 9, 0))                        
    return new_brick
            
def hot_brick(t):
    print(t)
    brick = []
    for _ in range(9):
        brick.append([25] * 10)
    brick.append([90] * 10)
    for step in range(t):
        brick = evolve_brick(brick)
    for row in brick:
        print(row)
    return brick

