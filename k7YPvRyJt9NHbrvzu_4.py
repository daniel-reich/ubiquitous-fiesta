
def football(score,curr=0,point=[2,3,6,7,8]):
    total = 0
    if curr == score: return 1
    if curr > score: return 0
    else:
        for i in range(len(point)):
            total += football(score,curr+point[i],point[i:])
        return total

