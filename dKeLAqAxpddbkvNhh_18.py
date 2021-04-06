
def group_seats(lst, n):
    l = []
    for row in lst:
        r = []
        empty = 0
        for seat in row:
            if seat == 0:
                empty += 1
            else:
                empty = 0
            r.append(empty)
        l.append(r)
    return sum([seat // n for row in l for seat in row ])

