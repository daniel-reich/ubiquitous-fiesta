
KNIGHT = ((-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1))
def knight_bfs(a, b, c, d):
    data = {(a, b)}
    result = 0
    while (c, d) not in data:
        result += 1
        newdata = set()
        for x, y in data:
            for dx, dy in KNIGHT:
                if 0<x+dx<9 and 0<y+dy<9:
                    newdata.add((x+dx, y+dy))
        data = newdata
    return result

