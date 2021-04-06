
def award_prizes(names):
    L = [[k, v] for k, v in names.items()]
    L.sort(key=lambda x: -x[1])
    gold = L.pop(0)[0]
    silver = L.pop(0)[0]
    bronze = L.pop(0)[0]
    ans = {gold: "Gold", silver: "Silver", bronze: "Bronze"}
    for name in L:
        ans[name[0]] = "Participation"
    return ans

