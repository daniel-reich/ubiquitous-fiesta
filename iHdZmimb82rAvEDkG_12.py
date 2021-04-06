
def bitwise_index(lst):
    largest = -2**31
    idx = -1
    for i in range(len(lst)):
        a = lst[i]
        if a > largest and (a // 2) * 2 == a:
            largest = a
            idx = i
    if idx < 0:
        return "No even integer found!"
    parity = "even" if (idx // 2) * 2 == idx else "odd"
    return {"@" + parity + " index " + str(idx): largest}

