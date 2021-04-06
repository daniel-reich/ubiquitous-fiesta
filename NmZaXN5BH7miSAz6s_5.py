
def climbing_leaderboard(ran, pla):
​
    def position(ran, pla, res):
        cnt = 1; pos = [(ran[0], cnt)]
        for i in range(1, len(ran)):
            if ran[i]-ran[i-1] == 0: pos.append((ran[i], cnt))
            else: cnt += 1; pos.append((ran[i], cnt))
        for i in range(len(ran)):
            if pos[i][0] == pla: res.append(pos[i][1]); return
​
    res = []
    for i in range(len(pla)):
        ran += [pla[i]]
        position(sorted(ran, reverse = True), pla[i], res)
    
    return res

