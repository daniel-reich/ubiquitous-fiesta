
def award_prizes(dic):
    inv_dic = {v: k for k, v in dic.items()}
    name = []
    a = []
    partc = []
    for i in dic.values():
        a = a + [i]
        a.sort()
    for i in a: 
        if i in inv_dic.keys():
            name = name + [inv_dic[i]]
        namelen = len(name)
    for p in range(0, (namelen-3)):
        partc = partc + [name[p]]
    first_place = name[-1]
    second_place = name[-2]
    third_place = name[-3] 
​
    winners = {}
    winners.setdefault(first_place, "Gold")
    winners.setdefault(second_place, "Silver")
    winners.setdefault(third_place, "Bronze")
    for i in partc:
        winners.setdefault(i, "Participation")
    return winners

