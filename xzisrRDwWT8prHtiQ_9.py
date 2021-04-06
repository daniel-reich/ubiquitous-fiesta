
def difference_two(lst):
    pairs = []
    for i, x in enumerate(sorted(lst)):
        for y in lst[i+1:]:
            if y == x + 2:
                pairs.append([x,y])
    return pairs

