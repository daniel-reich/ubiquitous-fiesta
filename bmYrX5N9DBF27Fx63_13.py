
def greatest_impact(lst):
    worst = []
    for idx, i in enumerate(lst):
        i.pop(0)
        if i[1] == 3:
            lst[idx][1] = 10
        elif i[1] == 2:
            lst[idx][1] = 5.5
        if len(set(i)) != 1:
            for pos in range(3):
                if i[pos] == min(i):
                    worst.append(pos)
    if worst:
        return ['Weather', 'Meals', 'Sleep'][max(worst, key=worst.count)]
    return 'Nothing'

