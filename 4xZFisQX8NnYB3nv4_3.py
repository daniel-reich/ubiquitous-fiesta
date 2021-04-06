
def maximum_seating(lst):
    lst = [0, 0] + lst + [0, 0]
    newly_filled = 0
    for idx, i in enumerate(lst[2:], 2):
        if i == 0 and lst[idx-2:idx] == [0, 0] and lst[idx+1:idx+3] == [0, 0]:
            lst[idx] = 1
            newly_filled += 1
    return newly_filled

