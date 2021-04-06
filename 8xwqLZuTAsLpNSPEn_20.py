
def award_prizes(names):
    lst = sorted([(val, key) for key, val in names.items()], reverse=True)
    names[lst[0][1]] = 'Gold'
    names[lst[1][1]] = 'Silver'
    names[lst[2][1]] = 'Bronze'
    for i in range(3, len(lst)):
        names[lst[i][1]] = 'Participation'
    return names

