
def get_primiera_score(deck):
    from collections import Counter
    c = Counter([i[-1] for i in deck])
    print(c)
    cards = ['d','h','s','c']
    for i in cards:
        if i not in c.keys():
            return 0
​
    points = {
        'A': 16,
        '7': 21,
        '6': 18,
        '2': 12,
        '3': 13,
        '4': 14,
        '5': 15,
        'J': 10,
        'K': 10,
        'Q': 10,
    }
    score=[]
    for c in cards:
        lst=[]
        for i in deck:
            if i[-1] == c:
                lst.append(points[i[0]])
        score.append(max(lst))
    return sum(score)

