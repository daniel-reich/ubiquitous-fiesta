
def bowling(lst: list) -> int:
    tot, turn = 0, 0
    first = True
    for i, v in enumerate(lst):
        if turn == 10:
            break
        if v == 10 and first:
            tot += v + lst[i+1] + lst[i+2]
            turn += 1
        elif v < 10 and first:
            tot += v
            first = False
        elif not first:
            turn += 1
            first = True
            tot += v
            if lst[i-1] + v == 10:
                tot += lst[i+1]
    return tot

