
import copy
​
def knight_bfs(a, b, c, d):
    move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    st, end = [a, b], [c, d]; past, count, last = {tuple(st):True}, 0, [st]
    while tuple(end) not in past:
        jump = copy.deepcopy(last); last = []
        for home in jump:
            for new in move:
                x, y = home[0]+new[0], home[1]+new[1]
                if 1<=x<=8 and 1<=y<=8 and (x,y) not in past:
                    past[(x,y)] = True; last.append([x,y])
        count += 1
    return count

