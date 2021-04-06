
def count_repetitions(lst):
    result = {}
    a = sorted([lst.count(i) for i in set(lst)])[::-1]
    for i in a:
        for y in set(lst):
            if lst.count(y) == i:
                result[y] = i
    return result

