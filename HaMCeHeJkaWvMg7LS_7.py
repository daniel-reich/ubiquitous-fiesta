
def sun_loungers(beach):
    count = vacant = 0
    empty = False
    if "1" not in beach:
        k = len(beach)
        if k > 1:
            k = (k + 1) // 2
        return k
    left_1 = beach.index("1")
    count += left_1 // 2
    right_1 = len(beach) - 1
    while beach[right_1] != "1":
        right_1 -= 1
    count += (len(beach) - 1 - right_1) // 2
    for x in beach[left_1: right_1 + 1]:
        if x == "1":
            k, rem = divmod(vacant, 2)
            if k and not rem:
                k -= 1
            count += k
            empty = False
            vacant = 0
        else:
            if empty:
                vacant += 1
            else:
                empty = True
                vacant = 1
    return count

