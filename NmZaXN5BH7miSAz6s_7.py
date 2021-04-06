
def climbing_leaderboard(ranked, player):
    ans=[]
    for i in player:
        new=ranked.copy()
        new.append(i)
        new.sort(reverse=True)
        r=1
        for a in range(1,len(new)):
            if new[0]==i:
                ans.append(1)
                break
            if new[a-1]!=new[a]:
                r+=1
            if new[a]==i:
                ans.append(r)
                break
    return ans

