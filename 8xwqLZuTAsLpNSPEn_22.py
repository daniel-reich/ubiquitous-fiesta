
def award_prizes(names):
    lst = [list(pair) for pair in names.items()]
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    awards = ('Gold', 'Silver', 'Bronze', 'Participation')
    for x in range(3):
        sorted_lst[x][1] = awards[x]
    if len(names.keys()) > 3:
        for part in sorted_lst[3:]:
            part[1] = awards[3]
    return dict(sorted_lst)

