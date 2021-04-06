
def hot_brick(t):
    br = [[25]*10 for _ in range(9)] + [[90]*10]
    for dt in range(t):
        brt = [[0]*10 for _ in range(9)] +[[90]*10]
        for r in range(9):
            for c in range(10):
                temp_sum = br[r][c]
                for dr, dc in [(0,1),(1,0),(1,1),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)]:
                    y, x = r + dr, c + dc
                    temp_sum += br[y][x] if 0 <= y < 10 and 0 <= x < 10 else 25
                brt[r][c] = int(round(temp_sum / 9))
        br = brt
    return br

