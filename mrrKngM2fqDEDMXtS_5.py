
def can_patch(bridge, planks):
    gaps = []
    ctr = 0
    a = 1
    while a < len(bridge)-1:
        if bridge[a] != 0:
            a += 1
        for j in range(a+1,len(bridge)):
            if sum(bridge[a:j+1]) != 0:
                if j-a != 1:
                    gaps.append(j-a)
                a = j
                break
        a += 1
​
    if len(gaps) == 0:
        return True
    gaps = sorted(gaps,reverse=True)
    planks = sorted(planks,reverse=True)
    for j in range(len(gaps)):
        for i in range(len(planks)):
            if gaps[j] - 1 == planks[i] or gaps[j] == planks[i]:
                del planks[i]
                gaps[j] = 0
                break
​
    return sum(gaps) == 0

