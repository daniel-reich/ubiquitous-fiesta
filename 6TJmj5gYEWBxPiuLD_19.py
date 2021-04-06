
def seating_students(lst):
    combos = (lst[0] / 2 - 1) * 2 + lst[0] / 2
    for seat in lst[1:]:
        empty = 2 if seat in (1, 2, lst[0]-1, lst[0]) else 3
        if seat + 2 in lst[1:]:
            empty -= 0.5
        if seat - 2 in lst[1:]:
            empty -= 0.5
        if seat % 2 == 0 and seat - 1 in lst[1:]:
            empty -= 0.5
        if seat % 2 != 0 and seat + 1 in lst[1:]:
            empty -= 0.5
        combos -= empty
​
    return int(combos)

