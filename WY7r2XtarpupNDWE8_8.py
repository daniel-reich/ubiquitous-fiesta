
def tower_of_hanoi_even(disks, move):
    pegs = [list(range(1, disks + 1))[::-1], [], []]
    m = 0
    while m < move:
        m += 1
        if m % 3 == 1:
            # make legal move between A and B
            p1, p2 = 0, 1
        elif m % 3 == 2:
            # make legal move between A and C
            p1, p2 = 0, 2
        else:
            # make legal move between B and C
            p1, p2 = 1, 2
        if len(pegs[p2]) == 0:
            pegs[p2].append(pegs[p1].pop())
        elif len(pegs[p1]) == 0:
            pegs[p1].append(pegs[p2].pop())
        else:
            if pegs[p1][-1] < pegs[p2][-1]:
                pegs[p2].append(pegs[p1].pop())
            else:
                pegs[p1].append(pegs[p2].pop())
    return tuple(pegs)
​
def tower_of_hanoi_odd(disks, move):
    pegs = [list(range(1, disks + 1))[::-1], [], []]
    m = 0
    while m < move:
        m += 1
        if m % 3 == 1:
            # make legal move between A and C
            p1, p2 = 0, 2
        elif m % 3 == 2:
            # make legal move between A and B
            p1, p2 = 0, 1
        else:
            # make legal move between B and C
            p1, p2 = 1, 2
        if len(pegs[p2]) == 0:
            pegs[p2].append(pegs[p1].pop())
        elif len(pegs[p1]) == 0:
            pegs[p1].append(pegs[p2].pop())
        else:
            if pegs[p1][-1] < pegs[p2][-1]:
                pegs[p2].append(pegs[p1].pop())
            else:
                pegs[p1].append(pegs[p2].pop())
    return tuple(pegs)
​
def tower_of_hanoi(disks, move):
    if disks == 1:
        return ([],[],[1])
    return tower_of_hanoi_even(disks, move) if disks % 2 == 0 else tower_of_hanoi_odd(disks, move)

