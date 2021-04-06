
def count_missing_nums(lst):
    count = 0
    new = sorted([int(i) for i in lst if i.isdecimal()])
    for x in range(new[0]+1, new[-1]):
        if x not in new:
            count += 1
    return count

