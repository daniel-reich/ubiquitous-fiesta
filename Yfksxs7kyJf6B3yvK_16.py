
def min_miss_pos(lst):
    n=1
    lst.sort()
    while True:
        if n not in lst:
            return n
        else:
            n+=1

