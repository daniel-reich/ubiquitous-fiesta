
def largest_even(lst):
    best = -1
    for i in lst:
        if not i%2 and i > best:
            best = i
    return best

