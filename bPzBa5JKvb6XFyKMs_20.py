
def get_primiera_score(deck):
    c = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    p = [16, 12, 13, 14, 15, 18, 21, 0, 0, 0, 10, 10, 10]
​
    points = [(i[1], p[c.index(i[0])]) for i in deck]
​
    points_sorted = {}
    for i in points:
        if i[0] not in points_sorted.keys():
            points_sorted[i[0]] = i[1]
        else:
            points_sorted[i[0]] = i[1] if i[1] > points_sorted[i[0]] else points_sorted[i[0]]
​
    if len(points_sorted.keys()) != 4:
        return 0
    else:
        return sum(points_sorted.values())

