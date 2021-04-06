
def numbers_to_ranges(lst):
    first = True
    result = []
    if len(lst) == 1:
        return [str(lst[0])]
    for x in range(len(lst)):
        current = lst[x]
        if first:
            start = current
        if x < len(lst) - 1:
            next = lst[x+1]
​
        elif x > len(lst) - 1:
            end = current
            result.append("{}-{}".format(start, end))
​
        if next-current != 1:
            end = current
            if start == end:
                result.append(str(start))
            else:
                result.append("{}-{}".format(start, end))
            first = True
        else:
            first = False
​
    return result

