
def digit_occurrences(start, end, digit):
    count = 0
    ranged = [str(i) for i in range(start, end + 1)]
    thing = "".join([i for i in ranged])
    splitted = [str(i) for i in thing]
    for i in splitted:
        if i == str(digit):
            count += 1
    return count

